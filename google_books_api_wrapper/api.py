import logging
from .rest_adapter import RestAdapter
from .constants import GOOGLE_BOOKS_API_URL
from .models import Book, HttpResult, BookSearchResultSet


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
            endpoint="volumes", ep_params={"q": search_term}
        )
        result_set = GoogleBooksApiParser.get_books_from_response(response)
        return result_set

    def get_book(self):
        pass


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
