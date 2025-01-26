from admin import Admin
from member import Member
from book import Book

admin = Admin("John Doe")

admin.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 5)
admin.add_book("1984", "George Orwell", "9780451524935", 3)
admin.add_book("Moby Dick", "Herman Melville", "9781503280786", 2)

admin.add_member("M001", "Alice Smith", "1234 Main St", "555-1234")
admin.add_member("M002", "Bob Johnson", "5678 Elm St", "555-5678")

catalog = admin.library.catalog

print("Search by Title: '1984'")
books = catalog.search_by_title("1984")
catalog.display_books(books)

print("\nSearch by Author: 'George Orwell'")
books = catalog.search_by_author("George Orwell")
catalog.display_books(books)

print("\nSearch by ISBN: '9781503280786'")
books = catalog.search_by_isbn("9781503280786")
catalog.display_books(books)

book = admin.library.books[0]
member = admin.library.members[0]
admin.library.borrow_book(book, member, "T001", "2025-01-26")

admin.library.return_book(book, member, "T002", "2025-02-01")
