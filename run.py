from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.search_book("atomic hdssadsadas")

print(response.get_all_results())
