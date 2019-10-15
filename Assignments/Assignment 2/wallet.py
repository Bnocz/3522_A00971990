from card import *
import json
class Wallet:

    def __init__(self, card_list):
        self.card_list = card_list


    def add_card(self):
        new_card = CardGenerator.generateCard()
        self.card_list.append(new_card)
        print("Successfully added: ")
        new_card.display_data()

    def display_wallet_by_type(self, type_):
        x = [card.display_data() if type(card) is type_ else '' for card in self.card_list]

    def display_wallet(self):
        for card in self.card_list:
            print(card.name)

    def search_wallet_by_name(self, query):
        search_result = self._retrieve_card_by_name(query)
        search_result.display_data()

    def search_wallet_by_number(self, query):
        search_result = self._retrieve_card_by_number(query)
        search_result.display_data()

    def _retrieve_card_by_name(self, name):
        requested_card = None
        requested_card = next((item for item in self.card_list if item.name == name), None)
        return requested_card

    def _retrieve_card_by_number(self, number):
        requested_card = None
        requested_card = next((item for item in self.card_list if item.number == number), None)
        return requested_card

    def remove_card(self, name):
        requested_card = self._retrieve_card_by_name(name)
        self.card_list.remove(requested_card)
        print(f"Removed {requested_card.name} from wallet")

    def write_to_file(self):
        with open("testfile.txt", 'w') as testfile:
            for i in self.card_list:
                testfile.write(json.dumps(self.card_list))



def generate_test_cards():
    card1 = CreditCard(name="Orange", card_face_name='orangutang',bank="Mastercard", number="21313213", expires="01/20", optional="")
    card2 = IdCard(name="Cherry", card_face_name='Potato Boy', bank="Mastercard", number="45489841", expires="09/21", optional="")
    card3 = LoyaltyCard(name='Banana', card_face_name='Jell-O', bank="Indigo", number="", card_type="Loyalty", optional="")


    test_cards = [
        card1, card2, card3
    ]

    return test_cards

def main():
    test_cards = generate_test_cards()
    test_wallet = Wallet(test_cards)
    user_input = None;
    while user_input != "q":
        print("Type add to add a card")
        user_input = input('>')
        if user_input == 'add':
            test_wallet.add_card()
        elif user_input == 'display':
            print(f"Enter 1 to view all Credit Cards")
            print(f"Enter 2 to view all Debit Cards")
            print(f"Enter 3 to view all Loyalty Cards")
        elif user_input == 'search':
            print("would you like to search by Card Name or Number?")
            user_input = input(">")
            if user_input == 'name':
                user_query = None;
                print("enter the card name")
                user_query = input('>')
                test_wallet.search_wallet_by_name(user_query)
            elif user_input == 'number':
                user_query = None;
                print("enter the card number")
                user_query = input('>')
                test_wallet.search_wallet_by_number(user_query)
            else:
                continue






if __name__ == '__main__':
    main()