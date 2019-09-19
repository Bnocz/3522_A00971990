import book

class Library:

    def __init__(self, book_list):
        self.book_list = book_list

    def find_books(self, call_number):
        for Book in self.book_list:
            if call_number == Book.call_number:
                return Book

    def add_book(self, new_book):
        if  new_book in self.book_list:
            return
        else:
            self.book_list.append(new_book)

    def remove_book(self, call_number):
        for Book in self.book_list:
            if call_number == Book.call_number:
                self.book_list.remove(Book)
            else:
                return

    def check_out(self, call_number):
        for Book in self.book_list:
            if call_number == Book.call_number and Book.num_copies >= 1:
                Book.num_copies -= 1
                print(f"Your book has been checked out, there are {Book.num_copies} left")
            elif call_number == Book.call_number and Book.num_copies == 0:
                print("Sorry that book is unavailable right now")

    def return_book(self, call_number):
        for Book in self.book_list:
            if call_number == Book.call_number:
                Book.num_copies += 1
                print(f"thanks for returning your book, there are now {Book.num_copies} left!")

    def display_available_books(self):
        for num in range(len(self.book_list)):
            print(self.book_list[num])


def main():
    book_list = [book.Book("Lord of the Rings", "1023", "JRR Tolkien", 1),
                 book.Book("Game of Thrones", 1033, "GRR Martin", 1),
                 book.Book("Harry Potter", 1212, "JK Rowling", 1)]
    biblioteca = Library(book_list)
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
        call_number = int(input("Enter the call number for the book: "))

        function_dict = {
            1: biblioteca.find_books(call_number),
            2: biblioteca.remove_book(call_number),
            3: biblioteca.check_out(call_number),
            4: biblioteca.return_book(call_number),
            5: biblioteca.display_available_books()
        }

        function_dict.get(choice)

if __name__ == '__main__':
    main()
