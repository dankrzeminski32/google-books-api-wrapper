from google_books_api_wrapper.models import Book

def test_book_model():
    book_obj = Book(title="atomic habits", authors=["james clear"])
    assert book_obj.title=="atomic habits"
    assert book_obj.authors[0]=="james clear"