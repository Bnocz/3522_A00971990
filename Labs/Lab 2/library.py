import item
import catalogue


def display_available_books(item_list):
    """
    prints item_list
    :param item_list: list of Item objects
    :return:
    """
    for Item in item_list:
        print(Item)


class Library:

    def __init__(self, item_list):
        self.item_list = item_list

    def check_out(self, call_number):
        """
        Searching through item list for call number and checks if num copies >= 1, if yes, reduces
        num_copies by 1 and if not, tells user that book is unavailable
        :param call_number: unique id for items
        :return:
        """
        for Item in self.item_list:
            if call_number == Item.call_number and Item.num_copies >= 1:
                Item.num_copies -= 1
                print(f"{Item.title} has been checked out, there are {Item.num_copies} left")
            elif call_number == Item.call_number and Item.num_copies == 0:
                print("Sorry that book is unavailable right now")

    def return_item(self, call_number):
        """
        search through item list and if found, increase num_copies by 1
        :param call_number: unique id for item
        :return:
        """
        for Item in self.item_list:
            if call_number == Item.call_number:
                Item.num_copies += 1
                print(f"thanks for returning your book, there are now {Item.num_copies} left!")


def main():
    """
    creates a list and fills it with Item objects. Creates a Library object, a catalogue object
    and a LibraryItemGenerator object. While loop runs until user inputs 0, other inputs demonstrate
    the possible functions within library and catalogue modules.
    :return:
    """
    item_list = [item.Book("Lord of the Rings", "1023.2323", "JRR Tolkien", 1),
                 item.Book("Game of Thrones", "1032.1212", "GRR Martin", 1),
                 item.Book("Harry Potter", "1111.2222", "JK Rowling", 1),
                 item.DVD("Pursuit of Happiness", "April 12, 1974", "NTSC", 1, "12121"),
                 item.Journal("National Geographic", 10, "Science", 1, "51232"),
                 item.Book("Game of Thrones", "1033", "GRR Martin", 1)]
    biblioteca = Library(item_list)
    catalogue_ = catalogue.Catalogue(item_list)
    generator_ = catalogue.LibraryItemGenerator(item_list)
    choice = 1
    while choice != 0:
        print("Welcome to Biblioteca self-service")
        print("If you would like to find a book, press 1")
        print("If you would like to request an item be removed press 2")
        print("If you would like to check out an item press 3")
        print("If you would like to return an item press 4")
        print("If you would like to add an item press 5")
        print("If you would like to browse the full catalogue press 6")
        print("If you would like to end self-service press 0")

        choice = int(input("what would you like to do? "))

        if choice == 1:
            title = input("Enter the title of the book you are looking for: ")
            if isinstance(title, str):
                catalogue_.find_item(title)
            else:
                return "Sorry, that is an invalid title"
        if choice == 2:
            call_number = input("Enter the call number for the book: ")
            if isinstance(call_number, str):
                catalogue_.remove_book(call_number)
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
            generator_.generate_item(item_list)
        if choice == 6:
            display_available_books(item_list)


if __name__ == '__main__':
    main()
