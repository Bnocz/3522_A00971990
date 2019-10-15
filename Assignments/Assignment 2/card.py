import abc
import unicodedata


class Card(abc.ABC):
    default_payment_data = {
        'name': None,
        'card_face_name': "",
        'bank': None,
        'number': "",
        'expires': None,
        'optional': ""
    }

    def __init__(self, **kwargs):
        self.card_data = Card.default_payment_data
        for key, item in kwargs.items():
            setattr(self, key, item)

    def __getitem__(self, key):
        return self.card_data[key]

    def display_data(self, **kwargs):
        if self.optional != "":
            print(f"Name: {self.name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")
            print(f"Card Type: {self['card_type']}")
            print(f"Notes: {self.optional}\n")
        else:
            print(f"Name: {self.name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")

    def __str__(self):
        return f"Nickname: {self['Name']}, Bank: {self['Bank']}, " \
        f"CardNum: {self['CardNum']}, Expires on: {self['Expires']}"

class IdCard(Card):

    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        if self.optional != "":
            print(f"Card Name: {self.name}")
            print(f"Name on Card: {self.card_face_name}")
            print(f"Issuer: {self.bank}")
            print(f"Card Number: {self.number}")
            print(f"Expires on: {self.expires}")
            print(f"Card Type: {self['card_type']}")
            print(f"Notes: {self.optional}\n")
        else:
            print(f"Card Name: {self.name}")
            print(f"Name on Card: {self.card_face_name}")
            print(f"Issuer: {self.bank}")
            print(f"Card Number: {self.number}")
            print(f"Expires on: {self.expires}\n")

    def __str__(self):
        return f"{self['Name']}"


class CreditCard(IdCard):
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        super().display_data()

    def __str__(self):
        return f"{self['Name']}"


class DebitCard(IdCard):
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        super().display_data()

    def __str__(self):
        return f"{self['Name']}"

class LoyaltyCard(Card):
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        super().display_data()


    def __str__(self):
        return f"{self['Name']}"

class BusinessCard(Card):
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):

        if self.optional != "":
            print(f"Card Name: {self.name}")
            print(f"Issuer name: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")
            print(f"Card Type: {self['card_type']}")
            print(f"Notes: {self.optional}\n")
        else:
            print(f"Name: {self.name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")

    def __str__(self):
        return f"{self['Name']}"



class PersonalIdentificationCard(IdCard):

    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        super().display_data()

    def __str__(self):
        return f"{self['Name']}"


class OtherCard(Card):
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        super().display_data()

    def __str__(self):
        return f"{self['Name']}"


class CardGenerator:
    @staticmethod
    def generate_card(**kwargs):
        for key, value in kwargs.items():
            card = IdCard(key, value)

    @staticmethod
    def generate_id_card(card_type, name, issuer):
        user_input = None;
        company = issuer
        user_input = input("Enter the name on the card: ")
        card_face_name = user_input
        user_input = input("Enter the card number: ")
        card_number = user_input
        user_input = input("Enter the expiry date(MM/DD): ")
        expiry_date = user_input
        user_input = input("Would you like to enter a note? (Leave blank if you don't want a note): ")
        optional = user_input
        if card_type == "debit":
            generated_card = DebitCard(name=name, card_face_name=card_face_name, bank=company, number=card_number,
                                       expires=expiry_date, optional=optional)
        elif card_type == "credit":
            generated_card = CreditCard(name=name, card_face_name=card_face_name, bank=company, number=card_number,
                                        expires=expiry_date, optional=optional)
        else:
            generated_card = PersonalIdentificationCard(name=name, card_face_name=card_face_name,
                                                        bank=company, number=card_number,
                                                        expires=expiry_date, optional=optional)

        return generated_card

    @staticmethod
    def generate_other_card(card_type, name, issuer):
        user_input = None;
        company = issuer
        user_input = input("Enter the card number (leave blank if the card has no number): ")
        card_number = user_input
        user_input = input("Would you like to enter a note? (Leave blank if you don't want a note): ")
        optional = user_input
        if card_type == "loyalty":
            generated_card = LoyaltyCard(name=name, bank=company, number=card_number,
                                         optional=optional)
        elif card_type == "business":
            card_type = "Business Card"
            generated_card = BusinessCard(name=name, bank=company, number=card_number,
                                         optional=optional)
        else:
            user_input = input("Enter the card type: ")
            card_type = user_input
            generated_card = OtherCard(name=name, bank=company, number=card_number,
                                         optional=optional, card_type=card_type)

        return generated_card

    @staticmethod
    def generateCard():
        user_input = None
        new_card = None
        print("Please enter a nickname for your card: ")
        user_input = input(">")
        name = user_input
        print("Who is the card issuer?(Or name, for business cards)")
        user_input = input(">")
        issuer = user_input
        while True:
            try:
                print(f"What kind of card is {name}? (Credit, Debit, Loyalty, Business, Other")
                user_input = input(">")
                user_input = user_input.casefold()
                if user_input == "credit" or user_input == "debit"or user_input == 'id':
                    new_card = CardGenerator.generate_id_card(user_input.casefold(), name, issuer)
                    return new_card
                elif user_input == "other" or user_input == 'loyalty' or \
                        user_input == 'business':
                    new_card = CardGenerator.generate_other_card(user_input.casefold().replace(" ", ""), name, issuer)
                    return new_card
                else:
                    raise ValueError
            except ValueError:
                print("Sorry, that's an invalid input")

    @staticmethod
    def add_cards():
        new_card = CardGenerator.generateCard()
        new_card.app

