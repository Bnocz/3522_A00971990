import item
import catalogue


class Library:

    def __init__(self, item_list):
        self.item_list = item_list

    def check_out(self, call_number):
        for Item in self.item_list:
            if call_number == Item.call_number and Item.num_copies >= 1:
                Item.num_copies -= 1
                print(f"{Item.title} has been checked out, there are {Item.num_copies} left")
            elif call_number == Item.call_number and Item.num_copies == 0:
                print("Sorry that book is unavailable right now")

    def return_book(self, call_number):
        for Item in self.item_list:
            if call_number == Item.call_number:
                Item.num_copies += 1
                print(f"thanks for returning your book, there are now {Item.num_copies} left!")

    def display_available_books(self):
        for num in range(len(self.item_list)):
            print(self.item_list[num])


def main():
    item_list = [item.Book("Lord of the Rings", "1023", "JRR Tolkien", 1),
                 item.Book("Game of Thrones", 1033, "GRR Martin", 1),
                 item.Book("Harry Potter", 1212, "JK Rowling", 1)]
    biblioteca = Library(item_list)
    catalogue_ = catalogue.Catalogue(item_list)
    generator_ = catalogue.LibraryItemGenerator(item_list)
    choice = 1
    while choice != 0:
        print("Welcome to Biblioteca self-service")
        print("If you would like to find a book, press 1")
        print("If you would like to request a book be removed press 2")
        print("If you would like to check out a book press 3")
        print("If you would like to return a book press 4")
        print("If you would like to browse the full list of books press 5")
        print("If you would like to end self-service press 0")

        choice = int(input("what would you like to do? "))

        if choice == 1:
            call_number = int(input("Enter the call number for the book: "))
            catalogue_.find_item(call_number)
        if choice == 2:
            call_number = int(input("Enter the call number for the book: "))
            generator_.generate_item(item_list)
        if choice == 3:
            call_number = int(input("Enter the call number for the book: "))
            biblioteca.check_out(call_number)
        if choice == 4:
            call_number = int(input("Enter the call number for the book: "))
            biblioteca.return_item(call_number)
        if choice == 5:
            biblioteca.display_available_books()


if __name__ == '__main__':
    main()
