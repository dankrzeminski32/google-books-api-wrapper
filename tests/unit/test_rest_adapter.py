import requests
from requests_mock.mocker import Mocker
from google_books_api_wrapper.rest_adapter import RestAdapter
from google_books_api_wrapper.constants import GOOGLE_BOOKS_API_URL
import logging

def test__do_good_request_returns_correct(requests_mock: Mocker):
    requests_mock.get("https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status_code=200,reason="")
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client._do("GET", "volumes").status_code
    assert {"test": "test"} == client._do("GET", "volumes").data    

def test_good_get_request_returns_correct(requests_mock: Mocker):
    requests_mock.get("https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status_code=200,reason="")
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client.get("volumes").status_code
    assert {"test": "test"} == client.get("volumes").data    
    
def test_good_post_request_returns_correct(requests_mock: Mocker):
    requests_mock.post("https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status_code=200,reason="")
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client.post("volumes").status_code
    assert {"test": "test"} == client.post("volumes").data    

