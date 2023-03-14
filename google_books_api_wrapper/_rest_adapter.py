"""
rest_adapter.py
====================================
The core module of my example project
"""
import requests
from .exceptions import GoogleBooksAPIException
from .models import HttpResult
from json import JSONDecodeError
import logging


class RestAdapter:
    """Low level Module used to handle incoming and outgoing web requests. Handles API configuration details.

    :param hostname: base web path of the API
    :type hostname: str
    :param ver: API version number, defaults to 'v1'
    :type ver: str, optional
    :param logger: Logging configuration, defaults to None
    :type logger: logging.Logger, optional
    """

    def __init__(self, hostname: str, ver: str = "v1", logger: logging.Logger = None):
        """RestAdapter Constructor"""
        self._logger = logger or logging.getLogger(__name__)
        self.url = "https://{}/{}/".format(hostname, ver)

    def _do(
        self, http_method: str, endpoint: str, ep_params: dict = None, data: dict = None
    ) -> HttpResult:
        """Private method used for sending and recieving requests

        :param http_method: http method for communicating with host (e.g. GET, POST)
        :type http_method: str
        :param endpoint: api resource endpoint (e.g. /books)
        :type endpoint: str
        :param ep_params: api parameters to send to endpoint, defaults to None
        :type ep_params: dict, optional
        :raises GoogleBooksAPIException: Exception raised when there is a failure to communicate with Google Books web endpoint
        :return: a HttpResult object
        :rtype: HttpResult
        """
        full_url = self.url + endpoint
        log_line_pre = f"method={http_method}, url={full_url}"
        log_line_post = ", ".join((log_line_pre, "success={}, status_code={}"))
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(
                method=http_method, url=full_url, params=ep_params, json=data
            )
        except requests.exceptions.RequestException as e:
            self._logger.error(msg=(str(e)))
            raise GoogleBooksAPIException("Request failed") from e
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            self._logger.error(msg=log_line_post.format(False, None, e))
            raise GoogleBooksAPIException("Bad JSON in response") from e
        is_success = 299 >= response.status_code >= 200  # 200 to 299 is OK
        log_line = log_line_post.format(is_success, response.status_code)
        if is_success:
            self._logger.debug(msg=log_line)
            return HttpResult(response.status_code, data=data_out)
        self._logger.error(msg=log_line)
        raise GoogleBooksAPIException(f"{response.status_code}: {response.reason}")

    def get(self, endpoint: str, ep_params: dict = None) -> HttpResult:
        """Sends a GET request to provided resource endpoint

        :param endpoint: api resource endpoint (e.g. /books)
        :type endpoint: str
        :param ep_params: api parameters to send to endpoint, defaults to None
        :type ep_params: dict, optional
        :return: a HttpResult object
        :rtype: HttpResult
        """
        return self._do(http_method="GET", endpoint=endpoint, ep_params=ep_params)

    def post(
        self, endpoint: str, ep_params: dict = None, data: dict = None
    ) -> HttpResult:
        """Sends a POST request to provided resource endpoint

        :param endpoint: api resource endpoint (e.g. /books)
        :type endpoint: str
        :param ep_params: api parameters to send to endpoint, defaults to None
        :type ep_params: dict, optional
        :param data: POST request data, defaults to None
        :type data: dict, optional
        :return: a HttpResult object
        :rtype: HttpResult
        """
        return self._do(
            http_method="POST", endpoint=endpoint, ep_params=ep_params, data=data
        )
