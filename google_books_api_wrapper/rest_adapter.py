
"""
rest_adapter.py
====================================
The core module of my example project
"""
import requests
from .exceptions import GoogleBooksAPIException
from .models import Result
from json import JSONDecodeError
import logging

class RestAdapter:
    """_summary_
    
    :param hostname: _description_
    :type hostname: str
    :param ver: _description_, defaults to 'v1'
    :type ver: str, optional
    :param logger: _description_, defaults to None
    :type logger: logging.Logger, optional
"""
    def __init__(self, hostname: str, ver: str = 'v1', logger: logging.Logger = None):
        """_summary_
        """
        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/{}/".format(hostname, ver)
        
    def _do(self, http_method: str, endpoint: str, ep_params: dict = None):
        full_url = self.url + endpoint
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, params=ep_params)
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise GoogleBooksAPIException("Request failed") from e
        try:
            data_out = response.json()
        except(ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise GoogleBooksAPIException("Bad JSON in response") from e
        is_success = 299 >= response.status_code >= 200     # 200 to 299 is OK
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            self._logger.debug(msg=log_line)
            return Result(response.status_code, message=response.reason, data=data_out)
        self._logger.error(msg=log_line)
        raise GoogleBooksAPIException(f"{response.status_code}: {response.reason}")
    
    def get(self, endpoint: str, ep_params: dict = None) -> list[dict]:
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)

    def post(self, endpoint: str, ep_params: dict = None, data: dict = None):
        return self._do(http_method='POST', endpoint=endpoint, ep_params=ep_params, data=data)