# Google Books API Wrapper for Python

This package wraps the [Google Books API](https://developers.google.com/books) in an easy to use Python interface. Use it to find comprehensive data on all books that peak your interest.

Begin by installing the package:

```bash
pip install google-books-api-wrapper
```

then import the required configuration object,

```python
from google_books_api_wrapper.api import GoogleBooksAPI
```

You can now use this object to **search** and **retreive** books,

```python
>>> client = GoogleBooksAPI()

>>> client.get_book_by_title("IT")
Book(title=It, authors=['Stephen King'])

>>> client.get_book_by_isbn13("9780670813025")
Book(title=It, authors=['Stephen King'])

>>> client.get_book_by_isbn10("0670813028")
Book(title=It, authors=['Stephen King'])

>>> simon_schuster_books = client.get_books_by_publisher("Simon & Schuster")
>>> simon_schuster_books.get_all_results()[:3]
[Book(title=Simon & Schuster's Guide to Dogs, authors=['Gino Pugnetti']), Book(title=Frankenstein, authors=['Mary Shelley']), Book(title=Why We Buy, authors=['Paco Underhill'])]

>>> fiction_books = client.get_books_by_subject("Fiction")
>>> fiction_books.get_all_results()[:3]
[Book(title=Lord of the Flies, authors=['William Golding']), Book(title=Amish Snow White, authors=['Rachel Stoltzfus']), Book(title=The Odyssey of Homer, authors=['Richmond Lattimore'])]

>>> stephen_king_books = client.get_books_by_author("Stephen King")
>>> stephen_king_books.total_results #Read Below about book return limit
40

>>> stephen_king_books.get_all_results()[:3]
[Book(title=It, authors=['Stephen King']), Book(title=1922, authors=['Stephen King']), Book(title=Elevation, authors=['Stephen King'])]
```
