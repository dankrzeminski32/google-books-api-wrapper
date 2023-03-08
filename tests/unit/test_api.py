from google_books_api_wrapper.api import GoogleBooksAPI
from google_books_api_wrapper.constants import GOOGLE_BOOKS_API_URL
from google_books_api_wrapper.models import Book, BookSearchResultSet
import responses


@responses.activate
def test_good_get_book_by_isbn13_returns_correct():
    responses.add(
        responses.GET,
        "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes",
        json={
    "kind": "books#volumes",
    "totalItems": 200,
    "items": [
        {"volumeInfo": {"title": "harry potter"}}]
        },
        status=200,
    )
    client = GoogleBooksAPI()
    book = client.get_book_by_isbn13(1234566)
    assert book.title=="harry potter"
    assert isinstance(book, Book)
    
@responses.activate
def test_good_search_request_returns_correct():
    responses.add(
        responses.GET,
        "https://" + GOOGLE_BOOKS_API_URL + "/v1/volumes",
        json={
    "kind": "books#volumes",
    "totalItems": 2,
    "items": [
        {"volumeInfo": {"title": "LOTR1"}},{"volumeInfo": {"title": "LOTR2"}}]
        },
        status=200,
    )
    client = GoogleBooksAPI()
    books: BookSearchResultSet = client.search_book(search_term="LOTR")
    assert books.total_results==2
    assert isinstance(books, BookSearchResultSet)
    assert books.get_best_match().title == "LOTR1"