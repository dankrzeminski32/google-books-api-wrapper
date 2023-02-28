.. Google Books API Wrapper documentation master file, created by
   sphinx-quickstart on Sat Feb 11 13:22:19 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Google Books API Wrapper's documentation!
====================================================

**google-books-api-wrapper** is a python web api wrapper for the Google Books api. I developed this mostly for using the unauthenticated requests for searching books and getting their relevant details.
This includes the authors, official title and subtitles, Publication date, Publisher, Genre, etc.utfu

.. toctree::
   :maxdepth: 2
   :caption: Contents:


GoogleBooksAPI Class
====================================================
.. autoclass:: google_books_api_wrapper.api.GoogleBooksAPI
    :members:

Book Class
====================================================
.. autoclass:: google_books_api_wrapper.models.Book
    :members:

HttpResult Class
====================================================
.. autoclass:: google_books_api_wrapper.models.HttpResult
    :members:

RestAdapter Class
====================================================
.. autoclass:: google_books_api_wrapper.rest_adapter.RestAdapter
    :members: