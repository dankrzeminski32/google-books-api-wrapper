import pytest
from tests.utils.file_reader import read_json_file
   
@pytest.fixture
def google_books_multiple_books_response_data():
    payload = read_json_file('valid_get_book_response.json')
    yield payload

@pytest.fixture
def google_books_no_books_in_response_data():
    payload = {
    "kind": "books#volumes",
    "totalItems": 0
}
    yield payload

    