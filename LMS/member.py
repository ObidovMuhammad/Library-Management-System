class Member:
    def __init__(self, member_id, name, address, phone):
        self.member_id = member_id
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"

    def update_details(self, name=None, address=None, phone=None):
        if name: self.name = name
        if address: self.address = address
        if phone: self.phone = phone
