from abc import ABC
from tabulate import tabulate
class AbstractPizza(ABC):

    def get_crust(self):
        pass

    def get_cheese(self):
        pass

    def get_toppings(self):
        pass

    def get_price(self):
        pass


class ConcretePizza(AbstractPizza):

    def get_crust(self):
        return "Python Pizza Signature Crust"

    def get_cheese(self):
        return ""

    def get_toppings(self):
        return ""

    def get_price(self):
        return 4.99


class Abstract_Pizza_Decorator(AbstractPizza):

    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza

    def get_crust(self):
        return self.decorated_pizza.get_crust()

    def get_price(self):
        return self.decorated_pizza.get_price()

    def get_cheese(self):
        return self.decorated_pizza.get_cheese()

    def get_toppings(self):
        return self.decorated_pizza.get_toppings()


class Mozarella(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Mozarella, '


class ParmigianoReggiano(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Parmigiano Reggiano, '


class VeganCheese(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Vegan Cheese, '



class Pepperoni(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 3

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Pepperoni, '


class Pineapple(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 2

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Pineapple, '


class Peppers(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Peppers, '


class Mushrooms(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Mushrooms, '


class FreshBasil(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 2

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Fresh Basil, '


class Spinach(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Spinach, '


class BeyondMeat(Abstract_Pizza_Decorator):
    def __init__(self, decorated_pizza):
        Abstract_Pizza_Decorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Beyond Meat, '

