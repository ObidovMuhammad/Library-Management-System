from book import Book
from member import Member
from transaction import Transaction
from catalog import Catalog

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []
        self.catalog = Catalog(self)

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member, transaction_id, date):
        if book.quantity > 0:
            transaction = Transaction(transaction_id, book, member, 'borrow', date)
            self.transactions.append(transaction)
            book.update_quantity(book.quantity - 1)
            print(f"Book {book.title} borrowed by {member.name}.")
        else:
            print("Sorry, the book is currently unavailable.")

    def return_book(self, book, member, transaction_id, date):
        transaction = Transaction(transaction_id, book, member, 'return', date)
        self.transactions.append(transaction)
        book.update_quantity(book.quantity + 1)
        print(f"Book {book.title} returned by {member.name}.")
