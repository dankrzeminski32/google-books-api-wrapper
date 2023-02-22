import logging
from .rest_adapter import RestAdapter
from .constants import GOOGLE_BOOKS_API_URL

class GoogleBooksAPI:
    """Wrapper around the Google Books REST API

    :param hostname: api hostname, defaults to "www.googleapis.com/books"
    :type hostname: str, optional
    :param ver: api version number, defaults to "v1"
    :type ver: str, optional
    :param logger: package logger, defaults to None
    :type logger: logging.Logger, optional
    """
    def __init__(self, hostname: str = GOOGLE_BOOKS_API_URL, ver: str = "v1", logger: logging.Logger = None):
        """ Constructor for GoogleBooksAPI
        """
        self._rest_adapter = RestAdapter(hostname, ver, logger)
        
    def search_book(self, search_term: str):
        return self._rest_adapter.get(endpoint="volumes", ep_params={"q": search_term})
    
    def get_book(self):
        pass
    
