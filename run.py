from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.get_book_by_title("IT")

print(response)