import logging
from typing import Dict, List

import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://api-v3.mbta.com/"
PARAMS = {}  # API key goes in here

RAIL_TYPE = 2
DIRECTION_ID = 0


def get_departure_list(station_id: str) -> List[dict]:
    """Calls the MBTA API and retrieves prediction data for selected station,
    along with stop, trip, and schedule data for train lines

    Args:
        station_id (str): "place-north" (North Station) or "place-south" (South Station).

    Returns:
        List[dict]: a list of formatted departure dicts
    """
    url = BASE_URL + "predictions"

    filters = {
        "filter[stop]": station_id,
        "filter[route_type]": RAIL_TYPE,
        "filter[direction_id]": DIRECTION_ID,
    }
    inclusions = {"include": "stop,trip,schedule"}

    logger.info("Requesting departure data from MBTA API!")

    res = requests.get(url, params={**PARAMS, **filters, **inclusions})

    res.raise_for_status()

    if not res.json()["data"]:
        return []

    return _format_departure_list(res.json())


def _format_departure_list(mbta_response: dict) -> List[dict]:
    """Filters and formats the response data from the MBTA API

    Args:
        mbta_response (dict): a list of data dicts from the MBTA API

    Returns:
        List[dict]: a list of formatted departure dicts
    """

    stops = [s for s in mbta_response["included"] if s["type"] == "stop"]
    trips = [t for t in mbta_response["included"] if t["type"] == "trip"]
    schedules = [s for s in mbta_response["included"] if s["type"] == "schedule"]

    # Filtering out trains that have already departed
    departure_list = [
        d for d in mbta_response["data"] if d["attributes"]["status"] != "Departed"
    ]

    formatted_departure_list = [
        _extract_departure_list(d, stops, trips, schedules) for d in departure_list
    ]

    formatted_departure_list.sort(key=lambda d: d["departure_time"])

    return formatted_departure_list


def _extract_departure_list(
    departure: dict, stops: list, trips: list, schedules: list
) -> Dict[str, str]:
    """Creates departure dicts by finding stop, trip and schedule response data

    Args:
        departure (dict): a departure prediction dict provided by MBTA API
        stops (list): a list of train stop dicts
        trips (list): a list of train trip dicts
        schedules (list): a list of train schedule dicts

    Returns:
        Dict[str, str]: a list of formatted departure dicts
    """

    name = departure["relationships"]["route"]["data"]["id"]
    status = departure["attributes"]["status"]

    stop_id = departure["relationships"]["stop"]["data"]["id"]
    stop_data = next(stop for stop in stops if stop["id"] == stop_id)
    platform_code = stop_data["attributes"]["platform_code"]

    trip_id = departure["relationships"]["trip"]["data"]["id"]
    trip_data = next(trip for trip in trips if trip["id"] == trip_id)
    train_no = trip_data["attributes"]["name"]

    schedule_id = departure["relationships"]["schedule"]["data"]["id"]
    schedule_data = next(
        schedule for schedule in schedules if schedule["id"] == schedule_id
    )
    departure_time = schedule_data["attributes"]["departure_time"]

    return {
        "name": name,
        "departure_time": departure_time,
        "status": status,
        "train_no": train_no,
        "platform_code": platform_code,
    }
