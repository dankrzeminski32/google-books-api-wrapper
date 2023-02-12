import logging
from rest_adapter import RestAdapter

class GoogleBooksAPI:
    def __init__(self, hostname: str = "www.googleapis.com/books", ver: str = "v1", logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, ver, logger)
        
    def search_book(self, search_term: str):
        return self._rest_adapter.get(endpoint="volumes", ep_params={'q': search_term})
    
    def get_book(self):
        pass
    

client = GoogleBooksAPI()
response = client.search_book("atomic habits")

    
print(response.data)
