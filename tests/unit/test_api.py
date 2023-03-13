from google_books_api_wrapper.api import GoogleBooksAPI 
from google_books_api_wrapper.constants import GOOGLE_BOOKS_API_URL
from google_books_api_wrapper.models import Book, BookSearchResultSet, GoogleBooksSearchParams, HttpResult
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
def test_good_get_book_by_isbn10_returns_correct():
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
    book = client.get_book_by_isbn10(1234566)
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
    
def test_generate_good_search_params():
    params = GoogleBooksSearchParams(title="test",isbn=20,publisher="penguin",author="dan",subject="fiction",search_term="wonder")
    assert "q=wonder+intitle:test+isbn:20+inpublisher:penguin+inauthor:dan+subject:fiction&maxResults=40" == params.generate()
    
def test_parser_get_books_good_request(google_books_multiple_books_response_data):
    resp = HttpResult(200, google_books_multiple_books_response_data)
    books = BookSearchResultSet.from_google_books_api_response(resp.data)
    assert books.total_results == 10
    

def test_parser_get_books_empty_request():
    resp = HttpResult(200, {"totalItems": 0})
    books = BookSearchResultSet.from_google_books_api_response(resp.data)
    assert books.total_results == 0
    assert books.get_all_results() == []
    assert books.get_best_match() == None

    

@responses.activate
def test_get_book_by_subject_produces_correct_request():
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
    book = client.get_books_by_subject("Fiction")
    assert responses.calls[0].request.params == {'maxResults': '40', 'q': ' subject:Fiction'}