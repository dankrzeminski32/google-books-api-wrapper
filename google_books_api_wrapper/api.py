import logging
from .rest_adapter import RestAdapter
from .constants import GOOGLE_BOOKS_API_URL, GoogleBookAPISearchFilters
from .models import Book, HttpResult, BookSearchResultSet
import urllib.parse


class GoogleBooksAPI:
    """Wrapper around the Google Books REST API

    :param hostname: api hostname, defaults to "www.googleapis.com/books"
    :type hostname: str, optional
    :param ver: api version number, defaults to "v1"
    :type ver: str, optional
    :param logger: package logger, defaults to None
    :type logger: logging.Logger, optional
    """

    def __init__(
        self,
        hostname: str = GOOGLE_BOOKS_API_URL,
        ver: str = "v1",
        logger: logging.Logger = None,
    ):
        """Constructor for GoogleBooksAPI"""
        self._rest_adapter = RestAdapter(hostname, ver, logger)

    def search_book(self, search_term: str) -> BookSearchResultSet:
        response = self._rest_adapter.get(
            endpoint="volumes", ep_params=GoogleBooksSearchParams(search_term=search_term).generate()
        )
        result_set = GoogleBooksApiParser.get_books_from_response(response)
        return result_set
    
    def get_book_by_isbn13(self, isbn13: int):
        response = self._rest_adapter.get(
            endpoint="volumes", ep_params={"q": "" + GoogleBookAPISearchFilters.ISBN + str(isbn13)}
        )
        result_set = GoogleBooksApiParser.get_books_from_response(response)
        return result_set
        
    def get_book_by_isbn10(self):
        pass
    
    def get_book_by_title(self):
        pass
    
    def get_books_by_author(self):
        pass
    
    def get_books_by_publisher(self):
        pass
    
    def get_books_by_subject(self):
        pass


class GoogleBooksSearchParams:
    def __init__(self, *, title:str=None, isbn: int=None, publisher: str=None, author: str=None, subject: str=None, search_term: str = ""):
        self.search_term = search_term
        self.title = title
        self.isbn = isbn
        self.publisher = publisher
        self.author = author
        self.subject = subject
    
    def generate(self):
        filters = self._get_used_filters()
        search_term_with_filters:str = None
        if len(filters) > 0:
            search_term_with_filters = self._get_search_term_with_filters()
        return {
            "q": search_term_with_filters or self.search_term
        }
        
    def _get_used_filters(self):
        used_properties = []
        for property in vars(self):
            if property == 'search_term':
                continue
            used_properties.append(property) if self.__getattribute__(property)!=None else ...
        return used_properties
            
    def _get_search_term_with_filters(self) -> str:
        search_term_with_filters: str = self.search_term
        for property in self._get_used_filters():
            search_term_with_filters = search_term_with_filters + GoogleBookAPISearchFilters[property.upper()] + str(self.__getattribute__(property))
        return urllib.parse.urlencode(search_term_with_filters, safe=':+')
        
class GoogleBooksApiParser:
    @staticmethod
    def get_books_from_response(response: HttpResult) -> BookSearchResultSet:
        book_results_from_web_api = response.data["items"] if "items" in response.data else []
        book_results = [
            Book.from_api_response_item(book_result)
            for book_result in book_results_from_web_api
        ]
        return BookSearchResultSet(books=book_results)

    @staticmethod
    def get_isbn_from_id_list(industry_ids: list[dict[str, str]], *, isbn_num: int) -> str:
        for id in industry_ids:
            if id["type"] == "ISBN_" + str(isbn_num):
                return id["identifier"]
        return None