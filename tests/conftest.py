import pytest
from tests.utils.file_reader import read_json_file
    
@pytest.fixture
def test_book_response_data():
    payload = read_json_file('valid_get_book_response.json')
    yield payload