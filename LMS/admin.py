from library import Library
from book import Book
from member import Member

class Admin:
    def __init__(self, name):
        self.name = name
        self.library = Library()

    def add_book(self, title, author, isbn, quantity):
        new_book = Book(title, author, isbn, quantity)
        self.library.add_book(new_book)
        print(f"Book {title} added to the library.")

    def add_member(self, member_id, name, address, phone):
        new_member = Member(member_id, name, address, phone)
        self.library.add_member(new_member)
        print(f"Member {name} added to the library.")
