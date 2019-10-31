from abc import ABC


class AbstractPizza(ABC):
    """
    Abstract pizza class to define methods all pizzas should have.
    """
    def get_crust(self):
        pass

    def get_cheese(self):
        pass

    def get_toppings(self):
        pass

    def get_price(self):
        pass


class ConcretePizza(AbstractPizza):
    """
    concrete base class that defines base case
    as well as constants
    """
    def get_crust(self):
        return "Python Pizza Signature Crust"

    def get_cheese(self):
        return ""

    def get_toppings(self):
        return ""

    def get_price(self):
        return 4.99


class AbstractPizzaDecorator(AbstractPizza):
    """

    """
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


class Mozarella(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Mozarella, '


class ParmigianoReggiano(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Parmigiano Reggiano, '


class VeganCheese(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 4.99

    def get_cheese(self):
        return self.decorated_pizza.get_cheese() + 'Vegan Cheese, '


class Pepperoni(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 3

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Pepperoni, '


class Pineapple(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 2

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Pineapple, '


class Peppers(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Peppers, '


class Mushrooms(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Mushrooms, '


class FreshBasil(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 2

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Fresh Basil, '


class Spinach(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Spinach, '


class BeyondMeat(AbstractPizzaDecorator):
    def __init__(self, decorated_pizza):
        AbstractPizzaDecorator.__init__(self, decorated_pizza)

    def get_price(self):
        return self.decorated_pizza.get_price() + 1.5

    def get_toppings(self):
        return self.decorated_pizza.get_toppings() + 'Beyond Meat, '
