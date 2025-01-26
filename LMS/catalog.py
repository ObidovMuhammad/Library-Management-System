class Catalog:
    def __init__(self, library):
        self.library = library

    def search_by_title(self, title):
        results = [book for book in self.library.books if title.lower() in book.title.lower()]
        return results

    def search_by_author(self, author):
        results = [book for book in self.library.books if author.lower() in book.author.lower()]
        return results

    def search_by_isbn(self, isbn):
        results = [book for book in self.library.books if book.isbn == isbn]
        return results

    def display_books(self, books):
        if books:
            for book in books:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - Quantity: {book.quantity}")
        else:
            print("No books found.")
