import item

class Catalogue:
    def __init__(self, item_list):
        self.book_list = item_list

    def find_item(self, call_number):
        for Item in self.item_list:
            if call_number == Item.call_number:
                return Item

    def add_book(self, new_item):
        if new_item in self.item_list:
            return
        else:
            self.item_list.append(new_item)

    def remove_book(self, call_number):
        for Item in self.item_list:
            if call_number == Item.call_number:
                self.item_list.remove(Item)
            else:
                return


class LibraryItemGenerator:
    def __init__(self, item_list):
        self.item_list = item_list

    def generate_item(self, item_list):
        print(f"what kind of item would you like to make?\n ")
        print(f"1. Book")
        print(f"2. DVD")
        print(f"3. Journal")
        choice = int(input("Your selection? "))
        if choice == 1:
            print("Please enter the Title, Call Number, and Author")
            item_ = item.Book("", 0, "", 0)
            item_.title = input("Title?")
            item_.call_number = int(input("Call Number?"))
            item_.author = input("Author?")
            item_.num_copies = 1
            self.item_list.append(item_)
        if choice == 2:
            print("Please enter the title, call number, release_date, and region_code")
            item_ = item.DVD("", 0, "", 0)
            item_.title = input("Title?")
            item_.call_number = int(input("call number?"))
            item_.release_date = input("release date?")
            item_.region_code = input("region code?")
            item_.num_copies = 1
            self.item_list.append(item_)
        if choice == 3:
            print("Please enter the title, call_number, issue, and publisher")
            item_ = item.Journal("", 0, "", 0)
            item_.title = input("Title?")
            item_.call_number = int(input("call number?"))
            item_.issue = input("issue?")
            item_.publisher = input("publisher?")
            item_.num_copies = 1
            self.item_list.append(item_)
        else:
            print("Sorry, that's an invalid option")
