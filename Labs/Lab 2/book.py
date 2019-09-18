class Book:

    def __init__(self, title, call_number, author, num_copies):
        self.title = title
        self.call_number = call_number
        self.author = author
        self.num_copies = num_copies

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Number of Copies: {self.num_copies}, " \
               f"Call Number: {self.call_number}"

    def check_availability(self, num_copies):
        if self.num_copies >= 1:
            return True
        else:
            return False
