class Transaction:
    def __init__(self, transaction_id, book, member, action, date):
        self.transaction_id = transaction_id
        self.book = book
        self.member = member
        self.action = action
        self.date = date

    def __str__(self):
        return f"Transaction ID: {self.transaction_id} | {self.action.capitalize()} | Book: {self.book.title} by {self.book.author} | Member: {self.member.name}"
