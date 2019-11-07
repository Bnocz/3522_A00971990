import item
import catalogue




class Library:
    """
    Class to simulate a library, takes care of lending
    has methods for users to check_out, and return items
    """

    def display_available_books(self):
        """
        prints item_list
        :param item_list: list of Item objects
        :return:
        """
        [print(item_) for item_ in self.item_list]

    def __init__(self, item_list):
        self.item_list = item_list

    def check_out(self, call_number):
        """
        Searching through item list for call number and checks if num copies >= 1, if yes, reduces
        num_copies by 1 and if not, tells user that book is unavailable
        :param call_number: unique id for items
        :return:
        """
        item_copy_cata = catalogue.Catalogue(self.item_list)
        for Item in self.item_list:
            if call_number == Item.call_number and Item.num_copies >= 1:
                item_copy_cata.decrement_copy(Item)
                print(f"{Item.title} has been checked out, there are {Item.num_copies} left")
            elif call_number == Item.call_number and Item.num_copies <= 0:
                print("Sorry that book is unavailable right now")

    def return_item(self, call_number):
        """
        search through item list and if found, increase num_copies by 1
        :param call_number: unique id for item
        :return:
        """
        item_copy_cata = catalogue.Catalogue(self.item_list)
        for Item in self.item_list:
            if call_number == Item.call_number:
                item_copy_cata.increment_copy(Item)
                print(f"thanks for returning your book, "
                      f"there are now {Item.num_copies} left!")


def main():
    """
    creates a list and fills it with Item objects. Creates a Library object, a catalogue object
    and a LibraryItemGenerator object. While loop runs until user inputs 0, other inputs demonstrate
    the possible functions within library and catalogue modules.
    :return:
    """
    item_list = [item.Book(title='got', author="grrm", num_copies=2,
                           call_number="12323"),
                 item.DVD(title='Shrek', release_date='2001',
                          region_code='ntsc', num_copies=0,
                          call_number="23123")]

    biblioteca = Library(item_list)
    catalogue_ = catalogue.Catalogue(item_list)
    book_factory = item.BookFactory()
    dvd_factory = item.DvdFactory()
    journal_factory = item.JournalFactory()
    choice = 1
    while choice != 0:
        print("\nWelcome to Biblioteca self-service")
        print("If you would like to find a book, press 1")
        print("If you would like to request an item be removed press 2")
        print("If you would like to check out an item press 3")
        print("If you would like to return an item press 4")
        print("If you would like to add an item press 5")
        print("If you would like to browse the full catalogue press 6")
        print("If you would like to end self-service press 0")

        choice = int(input("what would you like to do? \n"))

        if choice == 1:
            title = input("Enter the title of the book you are looking for: ")
            if isinstance(title, str):
                catalogue_.find_item(title)
            else:
                return "Sorry, that is an invalid title"
                input()
        if choice == 2:
            call_number = input("Enter the call number for the book: ")
            if isinstance(call_number, str):
                catalogue_.remove_item(call_number)
            else:
                return "That is an invalid call number"
        if choice == 3:
            call_number = input("Enter the call number for the book: ")
            if isinstance(call_number, str):
                biblioteca.check_out(call_number)
            else:
                return "That is an invalid call number"

        if choice == 4:
            call_number = input("Enter the call number for the book: ")
            if isinstance(call_number, str):
                biblioteca.return_item(call_number)
            else:
                return "that is an invalid call number"
        if choice == 5:
            print(f"what kind of item would you like to make?\n ")
            print(f"1. Book")
            print(f"2. DVD")
            print(f"3. Journal")
            choice = int(input(">"))
            if choice == 1:
                new_item = book_factory.create_item()
                catalogue_.add_item(new_item)
            if choice == 2:
                new_item = dvd_factory.create_item()
                catalogue_.add_item(new_item)
            if choice == 3:
                new_item = journal_factory.create_item()
                catalogue_.add_item(new_item)
        if choice == 6:
            biblioteca.display_available_books()


if __name__ == '__main__':
    main()
