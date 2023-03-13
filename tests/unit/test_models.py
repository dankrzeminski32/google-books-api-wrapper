from google_books_api_wrapper.models import Book, HttpResult, BookSearchResultSet
from collections.abc import Iterable
import pytest


def test_book_model():
    book_obj = Book(title="atomic habits", authors=["james clear"])
    assert book_obj.title == "atomic habits"
    assert book_obj.authors[0] == "james clear"

def test_get_book_from_google_books_api_response_book_item(google_books_multiple_books_response_data):
    fake_http_resp = HttpResult(200,google_books_multiple_books_response_data.get("items")[0])
    penguin_history_book = Book.from_google_books_api_response_book_item(fake_http_resp.data)
    assert penguin_history_book.title == "The Penguin History of the World"


def test_get_book_from_google_books_api_response_book_item_gets_isbn_13(google_books_multiple_books_response_data):
    fake_http_resp = HttpResult(200,google_books_multiple_books_response_data.get("items")[0])
    penguin_history_book = Book.from_google_books_api_response_book_item(fake_http_resp.data)
    assert penguin_history_book.ISBN_13 == "9781846144431"
    
def test_get_book_from_google_books_api_response_book_item_doesnt_find_isbn10_return_none(google_books_multiple_books_response_data):
    fake_http_resp = HttpResult(200,google_books_multiple_books_response_data.get("items")[0])
    penguin_history_book = Book.from_google_books_api_response_book_item(fake_http_resp.data)
    assert penguin_history_book.ISBN_10 == None
    
def test_get_book_search_result_set_correct_count_from_found_book_response(google_books_multiple_books_response_data):
    fake_http_resp = HttpResult(200,google_books_multiple_books_response_data)
    result_set = BookSearchResultSet.from_google_books_api_response(fake_http_resp.data)
    assert result_set.total_results == 10
    
def test_get_book_search_result_set_returns_no_data_from_empty_response(google_books_no_books_in_response_data):
    fake_http_resp = HttpResult(200,google_books_no_books_in_response_data)
    result_set = BookSearchResultSet.from_google_books_api_response(fake_http_resp.data)
    assert result_set.total_results == 0
    assert result_set.get_all_results() == []
    assert result_set.get_best_match() == None

def test_book_search_result_set_is_iterable(google_books_multiple_books_response_data):
    fake_http_resp = HttpResult(200,google_books_multiple_books_response_data)
    result_set = BookSearchResultSet.from_google_books_api_response(fake_http_resp.data)
    assert isinstance(result_set, Iterable) == True
        