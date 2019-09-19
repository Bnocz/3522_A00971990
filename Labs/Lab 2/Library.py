import book

class Library:

    def __init__(self, book_list):
        self.book_list = book_list

    def find_books(self, call_number):
        if call_number == book.Book.call_number:
            return book.Book.Title

    def add_book(self, new_book):
        if  new_book in self.book_list:
            return
        else:
            self.book_list.append(new_book)

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
        pass


def main():
    LoTR = book.Book("Lord of the Rings", "1023", "JRR Tolkien", 1)
    GoT = book.Book("Game of Thrones", 1033, "GRR Martin", 1)
    HP = book.Book("Harry Potter", 1212, "JK Rowling", 1)
    book_list = [LoTR, GoT]
    artemis = Library(book_list)
    artemis.return_book(1033)

if __name__ == '__main__':
    main()
