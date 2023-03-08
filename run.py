from google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()
response = client.search_book("john")

print(response.get_best_match().ISBN_13 + " " + response.get_best_match().title)
print(response.get_best_match().ISBN_10 + " " + response.get_best_match().title)


ten = client.get_book_by_isbn10(1610971027).ISBN_10
turdteen = client.get_book_by_isbn13(9781610971027).ISBN_13

print(ten)
print(turdteen)