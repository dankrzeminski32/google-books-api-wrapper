import requests
from google_books_wrapper.exceptions import GoogleBooksAPIException
from google_books_wrapper.models import Result
from json import JSONDecodeError

class RestAdapter:
    def __init__(self, hostname: str, ver: str = 'v1'):
        self.url = "https://{}/{}/".format(hostname, ver)
        
    def _do(self, http_method: str, endpoint: str, ep_params: dict = None):
        full_url = self.url + endpoint
        try:
            response = requests.request(method=http_method, url=full_url, params=ep_params)
        except requests.exceptions.RequestException as e:
            raise GoogleBooksAPIException("Request failed") from e
        try:
            data_out = response.json()
        except(ValueError, JSONDecodeError) as e:
            raise GoogleBooksAPIException("Bad JSON in response") from e
        if response.status_code >= 200 and response.status_code <= 299:     # OK
            return Result(response.status_code, message=response.reason, data=data_out)
        raise GoogleBooksAPIException(f"{response.status_code}: {response.reason}")
    
    def get(self, endpoint: str, ep_params: dict = None) -> list[dict]:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def post(self, endpoint: str, ep_params: dict = None, data: dict = None):
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)