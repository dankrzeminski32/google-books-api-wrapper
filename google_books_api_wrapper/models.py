from datetime import date


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
        subtitle: str = None,
        publisher: str = None,
        published_date: date = None,
        description: str = None,
        ISBN_13: str = None,
        ISBN_10: str = None,
        page_count: int = None,
        categories: list[str] = None,
        small_thumbnail: str = None,
        large_thumbnail: str = None,
    ):
        """Class Constructor"""
        self.title = title
        self.authors = authors
        self.subtitle = subtitle
        self.publisher = publisher
        self.published_date = published_date
        self.description = description
        self.ISBN_13 = ISBN_13
        self.ISBN_10 = ISBN_10
        self.page_count = page_count
        self.categories = categories
        self.small_thumbnail = small_thumbnail
        self.large_thumbnail = large_thumbnail
