import logging
from rest_adapter import RestAdapter

class GoogleBooksAPI:
    """Wrapper around the Google Books REST API

    :param hostname: api hostname, defaults to "www.googleapis.com/books"
    :type hostname: str, optional
    :param ver: api version number, defaults to "v1"
    :type ver: str, optional
    :param logger: package logger, defaults to None
    :type logger: logging.Logger, optional
    """
    def __init__(self, hostname: str = "www.googleapis.com/books", ver: str = "v1", logger: logging.Logger = None):
        """ Constructor for GoogleBooksAPI
        """
        self._rest_adapter = RestAdapter(hostname, ver, logger)
        
    def search_book():
        pass
    
    def get_book():
        pass
    