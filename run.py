from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.get_books_by_author("stephen king")

print(response)

for book in response:
    print(book)