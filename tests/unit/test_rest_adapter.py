import requests
import responses
from google_books_api_wrapper.rest_adapter import RestAdapter
from google_books_api_wrapper.constants import GOOGLE_BOOKS_API_URL
from google_books_api_wrapper.exceptions import GoogleBooksAPIException
import logging
import pytest

@responses.activate
def test__do_good_request_returns_correct():
    responses.add(responses.GET, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status=200)
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client._do("GET", "volumes").status_code
    assert {"test": "test"} == client._do("GET", "volumes").data
        
@responses.activate
def test_good_get_request_returns_correct():
    responses.add(responses.GET, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status=200)
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client.get("volumes").status_code
    assert {"test": "test"} == client.get("volumes").data    
    
@responses.activate
def test_good_post_request_returns_correct():
    responses.add(responses.POST, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", json={"test": "test"}, status=200)
    client = RestAdapter(GOOGLE_BOOKS_API_URL)
    assert 200 == client.post("volumes").status_code
    assert {"test": "test"} == client.post("volumes").data    

@responses.activate
def test_bad_get_request_returns_correct_exception():
    resp = responses.add(responses.GET, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes")
    resp.json={"test" "test"}
    with pytest.raises(GoogleBooksAPIException) as exc_info:
        client = RestAdapter(GOOGLE_BOOKS_API_URL)
        client.get("volumes").status_code
    assert str(exc_info.value) == 'Bad JSON in response'
        
@responses.activate
def test_good_get_request_returns_incorrect_json():
    responses.add(responses.GET, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", body=requests.exceptions.RequestException())
    with pytest.raises(GoogleBooksAPIException) as exc_info:
        client = RestAdapter(GOOGLE_BOOKS_API_URL)  
        client.get("volumes").status_code
    assert str(exc_info.value) == 'Request failed'

@responses.activate
def test_get_request_returns_invalid_status_code():
    responses.add(responses.GET, "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes", status=500, json={"test": "test"})
    with pytest.raises(GoogleBooksAPIException) as exc_info:
        client = RestAdapter(GOOGLE_BOOKS_API_URL)  
        client.get("volumes").status_code