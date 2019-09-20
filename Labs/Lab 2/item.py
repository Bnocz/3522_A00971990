class Item:

    def __init__(self, title, call_number, num_copies):
        self.title = title
        self.call_number = call_number
        self.num_copies = num_copies

    def __str__(self):
        return f"Title: {self.title}, Number of Copies: {self.num_copies}, " \
               f"Call Number: {self.call_number}"

    def check_availability(self, num_copies):
        if self.num_copies >= 1:
            return True
        else:
            return False


class DVD(Item):

    def __init__(self, title, release_date, region_code, num_copies, call_number):
        self.release_date = release_date
        self.region_code = region_code
        super().__init__(title, num_copies, call_number)

    def check_availability(self, num_copies):
        super().check_availability(num_copies)

    def __str__(self):
        return f"Title: {self.title}, release date: {self.release_date}, " \
               f"region code: {self.region_code}, Copies remaining: {self.num_copies}" \
               f" call_number: {self.call_number}"


class Journal(Item):

    def __init__(self, title, issue, publisher, num_copies, call_number):
        self.issue = issue
        self.publisher = publisher
        super().__init__(title, num_copies, call_number)

    def check_availability(self, num_copies):
        super().check_availability(num_copies)

    def __str__(self):
        return f"Title: {self.title}, issue: {self.issue}, " \
               f"publisher: {self.publisher}, Copies remaining: {self.num_copies}" \
               f" call_number: {self.call_number}"


class Book(Item):

    def __init__(self, title, call_number, author, num_copies):
        self.author = author
        super().__init__(title, call_number, num_copies)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Number of Copies: {self.num_copies}, " \
               f"Call Number: {self.call_number}"

    def check_availability(self, num_copies):
        if self.num_copies >= 1:
            return True
        else:
            return False
