import logging
from ._rest_adapter import RestAdapter
from .constants import GOOGLE_BOOKS_API_URL
from .models import Book, BookSearchResultSet, GoogleBooksSearchParams

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

    def search_book(
        self,
        search_term: str = "",
        isbn: str = None,
        title: str = None,
        author: str = None,
        publisher: str = None,
        subject: str = None,
    ) -> BookSearchResultSet:
        """Search for a book with optional filters

        :param search_term: General Search term relating to desired book, defaults to ""
        :type search_term: str, optional
        :param isbn: ISBN Identifier, defaults to None
        :type isbn: int, optional
        :param title: Book Title, defaults to None
        :type title: str, optional
        :param author: Book Author(s), defaults to None
        :type author: str, optional
        :param publisher: Book Publisher defaults to None
        :type publisher: str, optional
        :param subject: Book Subject, defaults to None
        :type subject: str, optional
        :return: A BookSearchResultSet objects
        :rtype: BookSearchResultSet
        """
        response = self._rest_adapter.get(
            endpoint="volumes",
            ep_params=GoogleBooksSearchParams(
                search_term=search_term,
                isbn=isbn,
                publisher=publisher,
                author=author,
                title=title,
                subject=subject,
            ).generate(),
        )
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set

    def get_book_by_isbn13(self, isbn13: str) -> Book:
        """Retrieve a book by ISBN13 Identifier.


        :param isbn13: ISBN13 Book Identiier
        :type isbn13: int
        :return: A Book Object
        :rtype: Book
        """
        return self._get_book_by_isbn(isbn13)

    def get_book_by_isbn10(self, isbn10: str) -> Book:
        """Retrieves a book by ISBN10 Identifier

        :param isbn10: ISBN10 Book Identifier
        :type isbn10: int
        :return: A Book object
        :rtype: Book
        """
        return self._get_book_by_isbn(isbn10)

    def get_book_by_title(self, title: str) -> Book:
        """Retrieves a book based on it's title

        :param title: Book title
        :type title: str
        :return: A Book object
        :rtype: Book
        """
        response = self._rest_adapter.get(
        endpoint="volumes",
        ep_params=GoogleBooksSearchParams(title=title).generate(),
        )
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set.get_best_match()

    
    def get_books_by_author(self, author: str) -> BookSearchResultSet:
        """Searches for books based on a particular author

        :param author: Book Author
        :type author: str
        :return: A BookSearchResultSet Object
        :rtype: BookSearchResultSet
        """
        response = self._rest_adapter.get(
        endpoint="volumes",
        ep_params=GoogleBooksSearchParams(author=author).generate(),
        )
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set

    def get_books_by_publisher(self, publisher: str) -> BookSearchResultSet:
        """Retrieves books that match a publisher string

        :param publisher: book publisher
        :type publisher: str
        :return: A BookSearchResultSet Object
        :rtype: BookSearchResultSet
        """
        response = self._rest_adapter.get(
        endpoint="volumes",
        ep_params=GoogleBooksSearchParams(publisher=publisher).generate(),
        )
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set

    def get_books_by_subject(self, subject: str) -> BookSearchResultSet:
        """Retrieve books that match a subject or genre

        :param subject: Subject or Genre of desired Books
        :type subject: str
        :return: A result set of Book items
        :rtype: BookSearchResultSet
        """
        response = self._rest_adapter.get(endpoint="volumes",
            ep_params=GoogleBooksSearchParams(
                subject=subject
            ).generate())
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set
    
    def _get_book_by_isbn(self, isbn: str) -> Book:
        """Base implementation of getting a book by isbn, used internally"""
        response = self._rest_adapter.get(
        endpoint="volumes",
        ep_params=GoogleBooksSearchParams(isbn=isbn).generate(),
        )
        result_set = BookSearchResultSet.from_google_books_api_response(response.data)
        return result_set.get_best_match()