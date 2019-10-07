from card import *
class Wallet:

    def __init__(self, card_list):
        self.card_list = card_list

    def add_card(self):
        new_card = CardGenerator.generateCard()
        self.card_list.append(new_card)
        print("Successfully added: ")
        new_card.display_data()

    def _retrieve_card_by_name(self, name):
        requested_card = None
        requested_card = next(name for card in self.card_list if card['Name'] == name)
        return requested_card

    def remove_card(self, name):
        requested_card = self._retrieve_card_by_name(name)
        self.card_list.remove(requested_card)
        print("Card removed: ")
        for card in self.card_list:
            print(card)


def generateTestCards():
    test_wallet = [
        PaymentCard(name="Apple", Bank="Visa", Number=54654564, Expires="01/20", Card_Type="Credit Card", business='Oppa'),
        PaymentCard(name="Orange", Bank="Mastercard", Number=21313213, Expires="01/20", Card_Type="Debit Card"),
        ]
    return test_wallet

def main():
    test_cards = generateTestCards()
    test_wallet = Wallet(test_cards)
    test_wallet.remove_card("Apple")


if __name__ == '__main__':
    main()