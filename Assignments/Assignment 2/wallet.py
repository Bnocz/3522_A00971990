from card import *
import json


class Wallet:
    '''
    class for digital wallet. Has methods to manage list of card objects
    '''
    def __init__(self, card_list):
        self.card_list = card_list

    def add_card(self):
        '''
        calls CardGenerator in card module. Appends returned card
        to card list, then displays the cards data in a readable form
        :return:
        '''
        new_card = CardGenerator.generate_card()
        self.card_list.append(new_card)
        print("Successfully added: ")
        new_card.display_data()

    def display_wallet_by_type(self, type_):
        '''
        List comprehension that displays card data based on the type of object that they are
        eg. CreditCard, DebitCard
        :param type_: Object type
        '''
        x = [card.display_data() if type(card) is type_ else '' for card in self.card_list]

    def display_wallet(self):
        '''
        displays everything in card list. Only prints name in-case list is massive, would be
        too difficult to read a full display of all data. User can use display_wallet_by_type
        for additional card details
        :return:
        '''
        for card in self.card_list:
            print(card.name)

    def search_wallet_by_name(self, query):
        '''
        searches the wallet by card nickname
        :param query: user input for search
        :return:
        '''
        search_result = self._retrieve_card_by_name(query)
        if search_result is None:
            print("No card found for entered name. Press Enter to return to main menu.")
            input()
        else:
            search_result.display_data()
            print("Press Enter to continue.")
            input()

    def search_wallet_by_number(self, query):
        '''
        searches wallet by card number
        :param query: user input for search
        :return:
        '''
        search_result = self._retrieve_card_by_number(query)
        if search_result is None:
            print("No card found for entered number. Press Enter to return to main menu.")
            input()
        else:
            search_result.display_data()
            print("Press Enter to continue.")
            input()

    def _retrieve_card_by_name(self, name):
        '''
        Uses an iterator to find a card based on nickname. Helper method for
        many other methods that need to find a card
        :param name: user input of card nickname
        '''
        requested_card = None
        requested_card = next((item for item in self.card_list if item.name == name), None)
        return requested_card

    def _retrieve_card_by_number(self, number):
        '''
        Uses an iterator to find a card based on number. Helper method for
        many other methods that need to find a card
        :param name: user input of card number
        '''
        requested_card = None
        requested_card = next((item for item in self.card_list if item.number == number), None)
        return requested_card

    def remove_card(self, name):
        '''
        takes user input, calls _retrieve_card_by_name and
        removes it from the card list
        :param name:
        :return:
        '''
        requested_card = self._retrieve_card_by_name(name)
        if requested_card is None:
            print("Could not find card with entered nickname")
            print("Press Enter to return to main menu")
            input()
        else:
            self.card_list.remove(requested_card)
            print(f"Removed {requested_card.name} from wallet\n")

    def write_to_file(self, path):
        '''
        writes card_list to a txt file in JSON format
        :param path:
        :return:
        '''
        with open("testfile.txt", 'w') as testfile:
            for i in self.card_list:
                testfile.write(json.dumps(self.card_list))


def generate_card_slots():
    '''
    creates an empty card list for wallet. Only used
    at start of program.
    '''

    card_slots = [
    ]

    return card_slots
