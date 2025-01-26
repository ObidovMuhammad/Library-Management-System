class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"Book: {self.title} by {self.author} (ISBN: {self.isbn})"
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
