import logging
from typing import List

import requests
from fastapi import FastAPI, status
from starlette.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from mbta_back_end.departure_utils import get_departure_list

app = FastAPI()
logger = logging.getLogger(__name__)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_main():
    return {"msg": "Hello World"}


@app.get("/departures/{station_id}")
def get_departures(station_id: str = "place-north") -> List[dict]:
    """Attempts to retrieve departure data from MBTA API

    Args:
        station_id (str, optional): "place-north" (North Station) or "place-sstat" (South Station). 
        Defaults to "place-north".

    Returns:
        List[dict]: a list of formatted departure dicts
    """
    try:
        departures = get_departure_list(station_id)
    except requests.RequestException:
        logger.exception("EXCEPTION")
        raise HTTPException(status_code=500, detail="Server Error")
    else:
        return departures
