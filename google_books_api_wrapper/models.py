from __future__ import annotations
from datetime import date
from .constants import GoogleBookAPISearchFilters
import urllib.parse

class HttpResult:
    """Low-level custom http result object

    :param status_code: http response status code (e.g. 200, 404, etc)
    :type status_code: int
    :param data: http json response data, defaults to None
    :type data: list[dict], optional
    """

    def __init__(self, status_code: int, data: dict = None):
        """Constructor"""
        self.status_code = int(status_code)
        self.data = data if data else {}


class Book:
    """Represents a Book object, data derived from Google Books Api Response

    :param title: Main title of the book
    :type title: str
    :param authors: Authors/Writers of the book
    :type authors: list[str]
    :param subtitle: Subtitle of the book, defaults to None
    :type subtitle: str, optional
    :param publisher: Book's official publisher, defaults to None
    :type publisher: str, optional
    :param published_date: Official book publication date, defaults to None
    :type published_date: date, optional
    :param description: Overall description of the book, defaults to None
    :type description: str, optional
    :param ISBN_13: Official ISBN-13 Identifier, defaults to None
    :type ISBN_13: str, optional
    :param ISBN_10: Official ISBN-10 Identifier, defaults to None
    :type ISBN_10: str, optional
    :param page_count: Number of pages in book, defaults to None
    :type page_count: int, optional
    :param categories: Book categories (e.g. horror, comedy, etc.), defaults to None
    :type categories: list[str], optional
    :param small_thumbnail: Small thumbnail img link from Google, defaults to None
    :type small_thumbnail: str, optional
    :param large_thumbnail: Large thumbnail img link from Google, defaults to None
    :type large_thumbnail: str, optional
    """

    def __init__(
        self,
        title: str,
        authors: list[str],
        id: str = None,
        subtitle: str = None,
        publisher: str = None,
        published_date: date = None,
        description: str = None,
        ISBN_13: str = None,
        ISBN_10: str = None,
        page_count: int = None,
        subjects: list[str] = None,
        small_thumbnail: str = None,
        large_thumbnail: str = None,
    ):
        """Class Constructor"""
        self.id = id
        self.title = title
        self.authors = authors
        self.subtitle = subtitle
        self.publisher = publisher
        self.published_date = published_date
        self.description = description
        self.ISBN_13 = ISBN_13
        self.ISBN_10 = ISBN_10
        self.page_count = page_count
        self.subjects = subjects
        self.small_thumbnail = small_thumbnail
        self.large_thumbnail = large_thumbnail

    @classmethod
    def from_google_books_api_response_book_item(cls, api_response_item: dict) -> Book:
        """Generates a Book object from Google Books Web API response

        :param api_response_item: Response item from hitting the Google Books API Endpoint
        :type api_response_item: HttpResult
        :return: A Book Object
        :rtype: Book
        """
        volume_id = api_response_item.get("id", None)
        volume_info = api_response_item.get("volumeInfo", {})
        industry_ids = volume_info.get("industryIdentifiers", [])
        image_links = volume_info.get("imageLinks", {})
        def get_isbn_from_id_list(
            industry_ids: list[dict[str, str]], *, isbn_num: int
        ) -> str:
            for id in industry_ids:
                if id["type"] == "ISBN_" + str(isbn_num):
                    return id["identifier"]
            return None
        return cls(
            id=volume_id,
            title=volume_info.get("title", None),
            authors=volume_info.get("authors", None),
            subtitle=volume_info.get("subtitle", None),
            publisher=volume_info.get("publisher", None),
            published_date=volume_info.get("publishedDate", None),
            description=volume_info.get("description", None),
            ISBN_13=get_isbn_from_id_list(
                industry_ids, isbn_num=13
            ),
            ISBN_10=get_isbn_from_id_list(
                industry_ids, isbn_num=10
            ),
            page_count=volume_info.get("pageCount", None),
            subjects=volume_info.get("categories", None),
            small_thumbnail=image_links.get("smallThumbnail", None),
            large_thumbnail=image_links.get("thumbnail", None),
        )

    def __repr__(self):
        return f"Book(title={self.title}, authors={self.authors})"

    def __str__(self):
        return f"Book(title={self.title}, authors={self.authors})"


class BookSearchResultSet:
    """Represents search results coming from the Google Books Web API

    :param books: A list of book objects, defaults to None
    :type books: list[Book], optional
    """

    def __init__(self, books: list[Book] = None):
        """Class Constructor."""
        self._books = books or []
        self._idx = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self._books[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx += 1
        return item
    
    @classmethod
    def from_google_books_api_response(cls, google_books_response_data: dict) -> BookSearchResultSet:
        book_results_from_web_api = (
            google_books_response_data["items"] if "items" in google_books_response_data else []
        )
        book_results = [
            Book.from_google_books_api_response_book_item(book_result)
            for book_result in book_results_from_web_api
        ]
        return cls(books=book_results)

        

    def get_best_match(self) -> Book | None:
        """Returns the closest match to the search query

        :return: A Book object
        :rtype: Book
        """
        return self._books[0] if self.total_results > 0 else None

    def get_all_results(self) -> list[Book]:
        """Returns a list of books returned for the search query

        :return: A list of Book objects
        :rtype: list[Book]
        """
        return self._books

    @property
    def total_results(self) -> int:
        """Total results found for search query

        :return: Number of results found
        :rtype: int
        """
        return len(self._books)

    def __repr__(self):
        return f"BookSearchResultSet(total_size={self.total_results})"

class GoogleBooksSearchParams:
    def __init__(
        self,
        *,
        title: str = None,
        isbn: str = None,
        publisher: str = None,
        author: str = None,
        subject: str = None,
        search_term: str = "",
    ):
        """Represents search parameters to be used on the API

        :param title: Book Title, defaults to None
        :type title: str, optional
        :param isbn: ISBN Number, defaults to None
        :type isbn: int, optional
        :param publisher: Book Publisher, defaults to None
        :type publisher: str, optional
        :param author: Book Author, defaults to None
        :type author: str, optional
        :param subject: Subject/Genre of Book, defaults to None
        :type subject: str, optional
        :param search_term: Book generalizedsearch term, defaults to ""
        :type search_term: str, optional
        """
        self.search_term = search_term
        self.title = title
        self.isbn = isbn
        self.publisher = publisher
        self.author = author
        self.subject = subject

    def generate(self) -> str:
        """Generates URL Query String based on item properties

        :return: Query String
        :rtype: str
        """
        filters = self._get_used_filters()
        search_term_with_filters: str = None
        if len(filters) > 0:
            search_term_with_filters = self._get_search_term_with_filters()
        return urllib.parse.urlencode({"q": search_term_with_filters or self.search_term, "maxResults": 40}, safe=":+")

    def _get_used_filters(self) -> list[str]:
        used_properties = []
        for property in vars(self):
            if property == "search_term":
                continue
            used_properties.append(property) if self.__getattribute__(
                property
            ) != None else ...
        return used_properties

    def _get_search_term_with_filters(self) -> str:
        search_term_with_filters: str = self.search_term
        for property in self._get_used_filters():
            search_term_with_filters = (
                search_term_with_filters
                + GoogleBookAPISearchFilters[property.upper()]
                + str(self.__getattribute__(property))
            )
        return search_term_with_filters
