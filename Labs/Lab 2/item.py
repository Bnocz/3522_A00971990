class Item:

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


class DVD(Item):

    def __init__(self, title, release_date, region_code, num_copies, call_number):
        self.title = title
        self.release_date = release_date
        self.region_code = region_code
        self.num_copies = num_copies
        self.ID = id

    def check_availability(self, num_copies):
        super().check_availability(num_copies)


class Journal(Item):

    def __init__(self, title, issue, publisher, num_copies, call_number):
        self.title = title
        self.issue = issue
        self.publisher = publisher
        self.num_copies = num_copies
        self.call_number = call_number

    def check_availability(self, num_copies):
        super().check_availability(num_copies)


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
