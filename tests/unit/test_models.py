from google_books_api_wrapper.models import Book, HttpResult, GoogleBooksSearchParams


def test_book_model():
    book_obj = Book(title="atomic habits", authors=["james clear"])
    assert book_obj.title == "atomic habits"
    assert book_obj.authors[0] == "james clear"

def test_get_book_from_api_response_item(test_book_response_data):
    fake_http_resp = HttpResult(200,test_book_response_data.get("items")[0])
    penguin_history_book = Book.from_api_response_item(fake_http_resp.data)
    assert penguin_history_book.title == "The Penguin History of the World"