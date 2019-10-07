import abc
import unicodedata


class Card(abc.ABC):
    default_payment_data = {
        'Name': None,
        'Bank': None,
        'CardNum': None,
        'Expires': None
    }
    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def __getitem__(self, key):
        pass

    def __str__(self):
        return f"Nickname: {self['Name']}, Bank: {self['Bank']}, " \
        f"CardNum: {self['CardNum']}, Expires on: {self['Expires']}"

class PaymentCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict(Card.default_payment_data)
        self.card_data = Card.default_payment_data
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data[key]

    def display_data(self, **kwargs):
        if self['optional'] != "":
            print(f"Name: {self['Name']}")
            print(f"Bank: {self['Bank']}")
            print(f"Card Number: {self['CardNum']}")
            print(f"Expires on: {self['Expires']}")
            print(f"Notes: {self['optional']}")
            print(f"Card Type: {self['Card_Type']}")
        else:
            print(f"Name: {self['Name']}")
            print(f"Bank: {self['Bank']}")
            print(f"Card Number: {self['CardNum']}")
            print(f"Expires on: {self['Expires']}")
            print(f"Card Type: {self['Card_Type']}")

    def __str__(self):
        return f"{self['kwargs']}"

class LoyaltyCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict(Card.default_payment_data)
        self.card_data = Card.default_payment_data
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data[key]

    def __str__(self):
        return str(f"{self.name}: {self.kwargs}")



class MiscCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict(Card.default_payment_data)
        self.card_data = Card.default_payment_data
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data[key]


class CardGenerator:
    @staticmethod
    def generate_card(**kwargs):
        for key, value in kwargs.items():
            card = PaymentCard(key, value)

    @staticmethod
    def generate_payment_card(card_type, name):
        user_input = None;
        user_input = input("Enter the bank your card is provided by: ")
        company = user_input
        user_input = input("Enter the card number: ")
        card_number = user_input
        user_input = input("Enter the expiry date(MM/DD): ")
        expiry_date = user_input
        user_input = input("Would you like to enter a note? (Leave blank if you don't want a note): ")
        optional = user_input
        if (card_type == "debit"):
            card_type = "Debit Card"
        elif(card_type == "credit"):
            card_type = "Credit Card"
        generated_card = PaymentCard(Name=name, Bank=company, Number=card_number,
                                     Expires=expiry_date, Card_Type=card_type, optional=optional)
        return generated_card

    @staticmethod
    def generate_other_card(card_type, name):
        user_input = None;
        user_input = input("*Enter the card issuer: (or name if it is a business card)")
        company = user_input
        user_input = input("Enter the card number: ")
        card_number = user_input
        user_input = input("Enter the expiry date(MM/DD): ")
        expiry_date = user_input
        if (card_type == "loyalty"):
            card_type = "Debit Card"
        elif(card_type == "business"):
            card_type = "Credit Card"
        generated_card = PaymentCard(Name=name, Bank=company, Number=card_number,
                                     Expires=expiry_date, Card_Type=card_type)
        return generated_card

    @staticmethod
    def generateCard():
        user_input = None;
        print("Please enter a nickname for your card: ")
        user_input = input(">")
        name = user_input
        print(f"What kind of card is {name}? (Credit, Debit, Loyalty, Business, Other")
        user_input = input(">")
        user_input = user_input.casefold()
        if user_input == "credit" or user_input == "debit":
            new_card =  CardGenerator.generate_payment_card(user_input.casefold(), name)
        elif user_input == "other" or user_input == 'loyalty' or user_input == 'business':
            new_card = CardGenerator.generate_other_card(user_input.casefold().replace(" ", ""), name)
        return new_card
    @staticmethod
    def add_cards():
        new_card = CardGenerator.generateCard()
        new_card.app

