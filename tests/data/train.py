
CHOO_CHOO = [{'name': 'CR-Newburyport', 'departure_time': '2020-06-22T22:50:00-04:00', 'status': 'Now boarding', 'train_no': '181', 'platform_code': '1'}, {'name': 'CR-Lowell', 'departure_time': '2020-06-22T22:55:00-04:00', 'status': 'On time', 'train_no': '345', 'platform_code': None}, {'name': 'CR-Haverhill', 'departure_time': '2020-06-22T23:00:00-04:00', 'status': 'On time', 'train_no': '227', 'platform_code': None}, {'name': 'CR-Fitchburg', 'departure_time': '2020-06-23T00:10:00-04:00', 'status': 'On time', 'train_no': '433', 'platform_code': None}, {'name': 'CR-Haverhill', 'departure_time': '2020-06-23T00:10:00-04:00', 'status': 'On time', 'train_no': '229', 'platform_code': None}, {'name': 'CR-Newburyport', 'departure_time': '2020-06-23T00:10:00-04:00', 'status': 'On time', 'train_no': '129', 'platform_code': None}, {'name': 'CR-Lowell', 'departure_time': '2020-06-23T00:15:00-04:00', 'status': 'On time', 'train_no': '347', 'platform_code': None}, {'name': 'CR-Newburyport', 'departure_time': '2020-06-23T00:15:00-04:00', 'status': 'On time', 'train_no': '183', 'platform_code': None}]

TEST_RESPONSE_DATA = {
    "data": [
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-433-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-433-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-433", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-347-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-347-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-347", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-345-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-345-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-345", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-229-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-229-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-229", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-227-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-227-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-227", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-183-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-183-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-183", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "On time",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-129-North Station-1",
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-129-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-129", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "Departed",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-223-North Station-01-1",
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-223-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station-01", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-223", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "Now boarding",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-181-North Station-01-1",
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-181-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station-01", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-181", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "Departed",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-127-North Station-03-1",
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-127-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station-03", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-127", "type": "trip"}},
                "vehicle": {"data": None},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "Departed",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-7423-North Station-09-1",
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-7423-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station-09", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-7423", "type": "trip"}},
                "vehicle": {"data": {"id": "1817", "type": "vehicle"}},
            },
            "type": "prediction",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": None,
                "direction_id": 0,
                "schedule_relationship": None,
                "status": "Departed",
                "stop_sequence": 1,
            },
            "id": "prediction-CR-Weekday-Summer-20-431-North Station-10-1",
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "schedule": {
                    "data": {
                        "id": "schedule-CR-Weekday-Summer-20-431-North Station-1",
                        "type": "schedule",
                    }
                },
                "stop": {"data": {"id": "North Station-10", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-431", "type": "trip"}},
                "vehicle": {"data": {"id": "1633", "type": "vehicle"}},
            },
            "type": "prediction",
        },
    ],
    "included": [
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Rockport",
                "name": "127",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-127",
            "links": {"self": "/trips/CR-Weekday-Summer-20-127"},
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Newburyport-4f18b08d-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Newburyport-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9810007", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Rockport",
                "name": "129",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-129",
            "links": {"self": "/trips/CR-Weekday-Summer-20-129"},
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Newburyport-0d0a9699-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Newburyport-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9810007", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Newburyport",
                "name": "181",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-181",
            "links": {"self": "/trips/CR-Weekday-Summer-20-181"},
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Newburyport-801f0591-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Newburyport-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9810002", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Newburyport",
                "name": "183",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-183",
            "links": {"self": "/trips/CR-Weekday-Summer-20-183"},
            "relationships": {
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Newburyport-801f0591-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Newburyport-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9810002", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Haverhill",
                "name": "223",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-223",
            "links": {"self": "/trips/CR-Weekday-Summer-20-223"},
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Haverhill-5a823277-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Haverhill-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9820002", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Haverhill",
                "name": "227",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-227",
            "links": {"self": "/trips/CR-Weekday-Summer-20-227"},
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Haverhill-5a823277-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Haverhill-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9820002", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Haverhill",
                "name": "229",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-229",
            "links": {"self": "/trips/CR-Weekday-Summer-20-229"},
            "relationships": {
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Haverhill-5a823277-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Haverhill-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9820002", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Lowell",
                "name": "345",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-345",
            "links": {"self": "/trips/CR-Weekday-Summer-20-345"},
            "relationships": {
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Lowell-78873e5a-0", "type": "route_pattern"}
                },
                "service": {"data": {"id": "CR-Wdy-Lowell-Smr-20", "type": "service"}},
                "shape": {"data": {"id": "9830006", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Lowell",
                "name": "347",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-347",
            "links": {"self": "/trips/CR-Weekday-Summer-20-347"},
            "relationships": {
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Lowell-78873e5a-0", "type": "route_pattern"}
                },
                "service": {"data": {"id": "CR-Wdy-Lowell-Smr-20", "type": "service"}},
                "shape": {"data": {"id": "9830006", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Wachusett",
                "name": "431",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-431",
            "links": {"self": "/trips/CR-Weekday-Summer-20-431"},
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Fitchburg-0196402e-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Fitchburg-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9840004", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Wachusett",
                "name": "433",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-433",
            "links": {"self": "/trips/CR-Weekday-Summer-20-433"},
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Fitchburg-0196402e-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Fitchburg-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9840004", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "bikes_allowed": 1,
                "block_id": "",
                "direction_id": 0,
                "headsign": "Wachusett",
                "name": "7423",
                "wheelchair_accessible": 1,
            },
            "id": "CR-Weekday-Summer-20-7423",
            "links": {"self": "/trips/CR-Weekday-Summer-20-7423"},
            "relationships": {
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "route_pattern": {
                    "data": {"id": "CR-Fitchburg-c7a7bb18-0", "type": "route_pattern"}
                },
                "service": {
                    "data": {"id": "CR-Wdy-Fitchburg-Smr-20", "type": "service"}
                },
                "shape": {"data": {"id": "9840004", "type": "shape"}},
            },
            "type": "trip",
        },
        {
            "attributes": {
                "address": None,
                "at_street": None,
                "description": "North Station - Commuter Rail",
                "latitude": 42.366417,
                "location_type": 0,
                "longitude": -71.062326,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": None,
                "platform_name": "Commuter Rail",
                "vehicle_type": 2,
                "wheelchair_boarding": 1,
            },
            "id": "North Station",
            "links": {"self": "/stops/North%20Station"},
            "relationships": {
                "child_stops": {},
                "facilities": {
                    "links": {"related": "/facilities/?filter[stop]=North%20Station"}
                },
                "parent_station": {"data": {"id": "place-north", "type": "stop"}},
                "recommended_transfers": {},
                "zone": {"data": {"id": "CR-zone-1A", "type": "zone"}},
            },
            "type": "stop",
        },
        {
            "attributes": {
                "address": None,
                "at_street": None,
                "description": "North Station - Commuter Rail - Track 1",
                "latitude": 42.366493,
                "location_type": 0,
                "longitude": -71.062829,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": "1",
                "platform_name": "Commuter Rail - Track 1",
                "vehicle_type": 2,
                "wheelchair_boarding": 1,
            },
            "id": "North Station-01",
            "links": {"self": "/stops/North%20Station-01"},
            "relationships": {
                "child_stops": {},
                "facilities": {
                    "links": {"related": "/facilities/?filter[stop]=North%20Station-01"}
                },
                "parent_station": {"data": {"id": "place-north", "type": "stop"}},
                "recommended_transfers": {},
                "zone": {"data": {"id": "CR-zone-1A", "type": "zone"}},
            },
            "type": "stop",
        },
        {
            "attributes": {
                "address": None,
                "at_street": None,
                "description": "North Station - Commuter Rail - Track 3",
                "latitude": 42.366535,
                "location_type": 0,
                "longitude": -71.06273,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": "3",
                "platform_name": "Commuter Rail - Track 3",
                "vehicle_type": 2,
                "wheelchair_boarding": 1,
            },
            "id": "North Station-03",
            "links": {"self": "/stops/North%20Station-03"},
            "relationships": {
                "child_stops": {},
                "facilities": {
                    "links": {"related": "/facilities/?filter[stop]=North%20Station-03"}
                },
                "parent_station": {"data": {"id": "place-north", "type": "stop"}},
                "recommended_transfers": {},
                "zone": {"data": {"id": "CR-zone-1A", "type": "zone"}},
            },
            "type": "stop",
        },
        {
            "attributes": {
                "address": None,
                "at_street": None,
                "description": "North Station - Commuter Rail - Track 9",
                "latitude": 42.366761,
                "location_type": 0,
                "longitude": -71.062365,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": "9",
                "platform_name": "Commuter Rail - Track 9",
                "vehicle_type": 2,
                "wheelchair_boarding": 1,
            },
            "id": "North Station-09",
            "links": {"self": "/stops/North%20Station-09"},
            "relationships": {
                "child_stops": {},
                "facilities": {
                    "links": {"related": "/facilities/?filter[stop]=North%20Station-09"}
                },
                "parent_station": {"data": {"id": "place-north", "type": "stop"}},
                "recommended_transfers": {},
                "zone": {"data": {"id": "CR-zone-1A", "type": "zone"}},
            },
            "type": "stop",
        },
        {
            "attributes": {
                "address": None,
                "at_street": None,
                "description": "North Station - Commuter Rail - Track 10",
                "latitude": 42.366761,
                "location_type": 0,
                "longitude": -71.062365,
                "municipality": "Boston",
                "name": "North Station",
                "on_street": None,
                "platform_code": "10",
                "platform_name": "Commuter Rail - Track 10",
                "vehicle_type": 2,
                "wheelchair_boarding": 1,
            },
            "id": "North Station-10",
            "links": {"self": "/stops/North%20Station-10"},
            "relationships": {
                "child_stops": {},
                "facilities": {
                    "links": {"related": "/facilities/?filter[stop]=North%20Station-10"}
                },
                "parent_station": {"data": {"id": "place-north", "type": "stop"}},
                "recommended_transfers": {},
                "zone": {"data": {"id": "CR-zone-1A", "type": "zone"}},
            },
            "type": "stop",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T22:20:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-127-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-127", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-23T00:10:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-129-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-129", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T22:50:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-181-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-181", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-23T00:15:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-183-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Newburyport", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-183", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T19:30:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-223-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-223", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T23:00:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-227-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-227", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-23T00:10:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-229-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Haverhill", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-229", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T22:55:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-345-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-345", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-23T00:15:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-347-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Lowell", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-347", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T22:40:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-431-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-431", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-23T00:10:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-433-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-433", "type": "trip"}},
            },
            "type": "schedule",
        },
        {
            "attributes": {
                "arrival_time": None,
                "departure_time": "2020-06-22T17:45:00-04:00",
                "direction_id": 0,
                "drop_off_type": 1,
                "pickup_type": 0,
                "stop_headsign": None,
                "stop_sequence": 1,
                "timepoint": True,
            },
            "id": "schedule-CR-Weekday-Summer-20-7423-North Station-1",
            "relationships": {
                "prediction": {},
                "route": {"data": {"id": "CR-Fitchburg", "type": "route"}},
                "stop": {"data": {"id": "North Station", "type": "stop"}},
                "trip": {"data": {"id": "CR-Weekday-Summer-20-7423", "type": "trip"}},
            },
            "type": "schedule",
        },
    ],
    "jsonapi": {"version": "1.0"},
}
