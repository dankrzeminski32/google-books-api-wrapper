from enum import Enum

GOOGLE_BOOKS_API_URL: str = "www.googleapis.com/books"


class GoogleBookAPISearchFilters(str, Enum):
    TITLE = "+intitle:"
    AUTHOR = "+inauthor:"
    PUBLISHER = "+inpublisher:"
    ISBN = "+isbn:"
    SUBJECT = "+subject:"
