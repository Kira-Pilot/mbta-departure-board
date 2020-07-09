from mbta_back_end.main import app
from fastapi.testclient import TestClient
from tests.data import train

import requests_mock

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_get_departures():

    endpoint_url = client.base_url + "/departures/place-north"

    with requests_mock.Mocker() as m:
        m.get("https://api-v3.mbta.com/predictions", json=train.TEST_RESPONSE_DATA)
        m.register_uri("GET", endpoint_url, real_http=True)
        response = client.get("/departures/place-north")

    assert response.status_code == 200
    assert response.json() == train.CHOO_CHOO


def test_failure_mode():

    endpoint_url = client.base_url + "/departures/place-north"

    with requests_mock.Mocker() as m:
        m.get("https://api-v3.mbta.com/predictions", status_code=500)
        m.register_uri("GET", endpoint_url, real_http=True)
        response = client.get("/departures/place-north")

    assert response.status_code == 500
