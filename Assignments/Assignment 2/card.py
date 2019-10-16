import abc
import unicodedata


class Card(abc.ABC):
    '''
    abstract class for a basic card with no data
    '''
    default_payment_data = {
        'name': None,
        'card_face_name': "",
        'bank': None,
        'number': "",
        'expires': None,
        'optional': ""
    }

    def __init__(self, **kwargs):
        '''
        takes input and sets attributes based on input
        :param kwargs: key word arguments entered by user
        '''
        self.card_data = Card.default_payment_data
        for key, item in kwargs.items():
            setattr(self, key, item)

    def __getitem__(self, key):
        '''
        Grabs attribute by key from object
        :param key: key for attribute
        :return:
        '''
        return self.card_data[key]

    def display_data(self, **kwargs):
        '''
        displays the card data, has optional arguments
        to only display if entered by user
        :param kwargs: key word arguments entered by user
        '''
        if self.optional != "":
            print(f"Name: {self.name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")
            print(f"Notes: {self.optional}\n")
        else:
            print(f"Name: {self.name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")

    def __str__(self):
        '''
        made redundant by display_data method. Used during testing
        '''
        return f"Nickname: {self['Name']}, Bank: {self['Bank']}, " \
                f"CardNum: {self['CardNum']}, Expires on: {self['Expires']}"


class IdCard(Card):
    '''
    parent class of all cards that have personal
    data, credit/debit/personalID/etc.
    '''
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
    '''
    template for less popular cards, or just really
    strange cards that wouldn't fit in the other categories.
    '''
    def __int__(self, **kwargs):
        super().__init__()

    def __getitem__(self, key):
        super().__getitem__()

    def display_data(self, **kwargs):
        if self.optional != "":
            print(f"Card Name: {self.name}")
            print(f"Name on Card: {self.card_face_name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")
            print(f"Expires on: {self.expires}")
            print(f"Notes: {self.optional}\n")
            print(f"Card Type: {self.card_type}")
        else:
            print(f"Card Name: {self.name}")
            print(f"Name on Card: {self.card_face_name}")
            print(f"Issuer: {self.bank}")
            if self.number != "":
                print(f"Number: {self.number}")
            print(f"Expires on: {self.expires}\n")
            print(f"Card Type: {self.card_type}")

    def __str__(self):
        return f"{self['Name']}"


class CardGenerator:
    '''
    Class that has methods which take user input to generate cards
    '''

    @staticmethod
    def generate_id_card(card_type, name, issuer):
        '''
        generates an id card object based on user input.
        :param card_type: parameter taken from generate_card to determine which card to create
        :param name: nickname user gave the card. Sort of an ID for the card
        :param issuer: The bank or person who gave the card, collected in generate_card
        :return DebitCard, CreditCard, PersonalIdentificationCard
        '''
        user_input = None;
        company = issuer
        user_input = input("Enter the name on the card: ")
        card_face_name = user_input
        user_input = input("Enter the card number: (leave blank if card has no number)")
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
        '''
        generates non-id cards, as well as "other" cards
        :param card_type: parameter taken from generate_card to determine which card to create
        :param name: nickname user gave the card. Sort of an ID for the card
        :param issuer: The bank or person who gave the card, collected in generate_card
        :return LoyaltyCard, BusinessCard or OtherCard
        '''
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
    def generate_card():
        '''
        gathers common data between cards, nickname the user has given the card,
        the issuer of the card, as well as the type of card it is, then passes this information
        onto the specialized generator methods
        '''
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
                print(f"What kind of card is {name}? (Credit, Debit, Loyalty, Business, ID, other)")
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


