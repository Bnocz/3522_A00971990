from abc import ABC


class Item(ABC):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __iter__(self):
        yield from self

    def __getitem__(self, key):
        return self.Item[key]

    def __str__(self):
        return f"Title: {self.title}, Number of Copies: {self.num_copies}, " \
               f"Call Number: {self.call_number}"

    def check_availability(self, num_copies):
        if self.num_copies >= 1:
            return True
        else:
            return False


class DVD(Item):

    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)

    def check_availability(self, num_copies):
        super().check_availability(num_copies)

    def __str__(self):
        return f"Title: {self.title}, Release Date: {self.release_date}, " \
               f"Region Code: {self.region_code}, Number of copies:" \
               f" {self.num_copies}" \
               f" Call Number: {self.call_number}"


class Journal(Item):

    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)

    def check_availability(self, num_copies):
        super().check_availability(num_copies)

    def __str__(self):
        return f"Title: {self.title}, issue: {self.issue}, " \
               f"publisher: {self.publisher}, Number of copies: " \
               f"{self.num_copies}" \
               f" call_number: {self.call_number}"


class Book(Item):

    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, " \
               f"Number of Copies:" \
               f" {self.num_copies}, " \
               f"Call Number: {self.call_number}"

    def check_availability(self, num_copies):
        if self.num_copies >= 1:
            return True
        else:
            return False


class ItemFactory(ABC):
    def create_item(self) -> Item:
        pass


class DvdFactory(ItemFactory):
        def create_item(self) -> Item:
            title = input("Enter the DVD title: ")
            release_date = input("Enter the release date: ")
            region_code = input("Enter the region code: ")
            call_number = input("Enter the call_number: ")
            return DVD(title=title, release_date=release_date,
                        region_code=region_code,
                        call_number=call_number, num_copies=1)


class BookFactory(ItemFactory):
    def create_item(self) -> Item:
        title = input("Enter the book title: ")
        author = input("Enter the Author: ")
        call_number = input("Enter the call number: ")
        return Book(title=title, author=author,
                    call_number=call_number, num_copies=1)


class JournalFactory(ItemFactory):
    def create_item(self) -> Item:
        title = input("Enter the journal title: ")
        issue = input("Enter the issue number: ")
        publisher = input("Enter the publisher: ")
        call_number = input("Enter the call number: ")
        return Journal(title=title, issue=issue, publisher=publisher,
                       call_number=call_number, num_copies=1)