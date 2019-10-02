import abc


class Card(abc.ABC):
    @abc.abstractmethod
    def __init__(self, **kwargs):
        pass

    @abc.abstractmethod
    def __getitem__(self, key):
        pass


class CreditCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict()
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data


class LoyaltyCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict()
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data


class MiscCard(Card):

    def __init__(self, **kwargs):
        self.card_data = dict()
        for key, item in kwargs.items():
            self.card_data[key] = item

    def __getitem__(self, key):
        return self.card_data


class CardGenerator:

    @staticmethod
    def generate_card():
        name = input("Enter name: ")
        card_number = input("Enter card number: ")
        return CreditCard(name=name, card_number=card_number)


def main():
    test = CardGenerator.generate_card()
    print(f'Name: {test["name"]}')


if __name__ == '__main__':
    main()