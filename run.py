from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.get_books_by_subject("fiction")

print(response.get_best_match().subjects)