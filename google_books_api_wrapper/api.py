import logging
from rest_adapter import RestAdapter

class GoogleBooksAPI:
    def __init__(self, hostname: str = "www.googleapis.com/books", ver: str = "v1", logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, ver, logger)
        
    def search_book():
        pass
    
    def get_book():
        pass
    