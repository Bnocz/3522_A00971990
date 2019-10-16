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

    def write_to_file(self, path):
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
        print("Welcome to your wallet!")
        print(f"Enter 'add' to add a card to your wallet")
        print(f"Enter 'remove' to remove a card from your wallet")
        print(f"Enter  'display' to view your wallet")
        print(f"Enter 'save' to save your wallet to a file")
        print(f"Enter 'q' to exit")
        user_input = input('>')
        user_input = user_input.casefold()
        if user_input == 'add':
            test_wallet.add_card()
        elif user_input == 'display':
            print(f"Enter 'Credit' to view all Credit Cards")
            print(f"Enter 'Debit' to view all Debit Cards")
            print(f"Enter 'Loyalty' to view all Loyalty Cards")
            print(f"Enter 'Business' to view all Business Cards")
            print(f"Enter 'ID' to view personal ID cards")
            print(f"Enter 'Other' to view all other cards")
            print(f"Leave blank if you just want to see the entire wallet")
            user_input = input(">")
            user_input = user_input.casefold()
            if user_input == 'credit':
                test_wallet.display_wallet_by_type(CreditCard)
                input("\nPress Enter to continue.")
            elif user_input == 'debit':
                test_wallet.display_wallet_by_type(DebitCard)
                input("\nPress Enter to continue.")
            elif user_input == 'loyalty':
                test_wallet.display_wallet_by_type(LoyaltyCard)
                input("\nPress Enter to continue.")
            elif user_input == 'business':
                test_wallet.display_wallet_by_type(BusinessCard)
                input("\nPress Enter to continue.")
            elif user_input == 'id':
                test_wallet.display_wallet_by_type(PersonalIdentificationCard)
                input("\nPress Enter to continue.")
            elif user_input == 'other':
                test_wallet.display_wallet_by_type(OtherCard)
                input("\nPress Enter to continue.")
            else:
                test_wallet.display_wallet()
                input("\nPress Enter to continue.")
        elif user_input == 'search':
            print("would you like to search by Card Name or Number?")
            user_input = input(">")
            user_input = user_input.casefold()
            if user_input == 'name':
                user_query = None;
                print("enter the card name")
                user_input = user_input.casefold()
                user_query = input('>')
                test_wallet.search_wallet_by_name(user_query)
            elif user_input == 'number':
                user_query = None;
                print("enter the card number")
                user_query = input('>')
                test_wallet.search_wallet_by_number(user_query)
            else:
                continue
        elif user_input == 'save':
            print("Enter a name for your textfile")
            path = input(">")
            print("Saving to file..")
            test_wallet.write_to_file(path+'txt')
            print(f"Saved to: {path+'txt'}")






if __name__ == '__main__':
    main()