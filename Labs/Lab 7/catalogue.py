import item


class Catalogue:
    """
    Catalogue class contains methods to add, remove, and find
    an item within the item_list.
    """
    def __init__(self, item_list):
        self.item_list = item_list

    @staticmethod
    def increment_copy(item_):
        item_.num_copies += 1

    @staticmethod
    def decrement_copy(item_):
        item_.num_copies -= 1

    def find_item(self, title):
        """
        searches through item_list and returns
        all Items with identical title
        :param title:
        :return:
        """
        return [print(Item) for Item in self.item_list if title == Item.title]

    def add_item(self, new_item):
        """
        Appends a book to the end of the list,
        replaced by LibraryItemGenerator for
        most uses.
        :param new_item: new Item object
        :return:
        """
        [self.item_list.append(new_item) for item in self.item_list
         if new_item not in self.item_list]

    def remove_item(self, call_number):
        """
        Iterates through list to see if call number matches
        any call number of items in list, then removes the
        item from the list.
        :param call_number: unique identifier for item
        :return:
        """
        [self.item_list.remove(Item) for Item in self.item_list]


'''class LibraryItemGenerator:
    """
    Asks user what kind of Item they would like to create, then
    takes user input for Item attributes, and appends generated
    item to the end of the item_list
    """
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
            item_.call_number = input("Call Number?")
            item_.author = input("Author?")
            item_.num_copies = 1
            self.item_list.append(item_)
        if choice == 2:
            print("Please enter the title, call number, release_date, and region_code")
            item_ = item.DVD("", 0, "", 0, 0)
            item_.title = input("Title?")
            item_.call_number = input("call number?")
            item_.release_date = input("release date?")
            item_.region_code = input("region code?")
            item_.num_copies = 1
            self.item_list.append(item_)
        if choice == 3:
            print("Please enter the title, call_number, issue, and publisher")
            item_ = item.Journal("", 0, "", 0, 0)
            item_.title = input("Title?")
            item_.call_number = input("call number?")
            item_.issue = input("issue?")
            item_.publisher = input("publisher?")
            item_.num_copies = 1
            self.item_list.append(item_)
        else:
            print("Sorry, that's an invalid option")'''
