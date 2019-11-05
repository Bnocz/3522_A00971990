from pizzashop import *
from custom_errors import *
import sys
import time
def main():
    """
    main method that drives the program.
    Has interface for user to decorate a
    ConcretePizza.
    :return:
    """
    user_input = 0
    print("riiiiiiiing")
    time.sleep(0.5)
    print("riiiiiiiing")
    time.sleep(0.5)
    print("Thanks for calling Python Pizza, could I get you a menu?\n")
    user_pizza = ConcretePizza()
    input("Press enter to view the menu")
    while user_input != 'bye':
        try:
            print("""\
                    *********   Menu *********
                    *------------------------*
                    *         Cheeses:       *
                    *------------------------*
                    *         Mozarella      *
                    *   Parmigiano Reggiano  *
                    *       Vegan Cheese     *
                    *------------------------*
                    *         Meats:         *
                    *------------------------*    
                    *        Pepperoni       *                            
                    *       Beyond Meat      *
                    *------------------------*   
                    *        Peppers         *
                    *        Pineapple       *
                    *        Mushrooms       *
                    *       Fresh Basil      *
                    *        Spinach         *
                    **************************
                    -All Pizza's come with our Python Pizza Signature Crust
                                """)
            print("Enter the ingredient you would like to add, or type 'check out' to see your total. Type 'Bye' to exit")
            user_input = input(">")
            user_input = user_input.casefold().replace(" ", "")
            if user_input == "checkout":
                check_out(user_pizza)
            elif user_input == "pepperoni":
                print("topping added!")
                user_pizza = Pepperoni(user_pizza)
            elif user_input == "mozzarella":
                print("topping added!")
                user_pizza = Mozarella(user_pizza)
            elif user_input == "parmigianoreggiano":
                print("topping added!")
                user_pizza = ParmigianoReggiano(user_pizza)
            elif user_input == "vegancheese":
                print("topping added!")
                user_pizza = VeganCheese(user_pizza)
            elif user_input == "peppers":
                print("topping added!")
                user_pizza = Peppers(user_pizza)
            elif user_input == "pineapple":
                print("topping added!")
                user_pizza = Pineapple(user_pizza)
            elif user_input == "mushrooms":
                print("topping added!")
                user_pizza = Mushrooms(user_pizza)
            elif user_input == "freshbasil" or "basil":
                print("topping added!")
                user_pizza = FreshBasil(user_pizza)
            elif user_input == "spinach":
                print("topping added!")
                user_pizza = Spinach(user_pizza)
            elif user_input == "beyondmeat":
                print("topping added!")
                user_pizza = Spinach(user_pizza)


        except InputError:
            print("Invalid Input")


def check_out(user_pizza):
    """
    checks if pizza has a cheese on it,
    if it does, prints out the pizza
    decorations, and ends program if user
    is happy with their pizza. Raises
    NotEnoughToppings if there is no
    cheese on the pizza
    :param user_pizza: decorated ConcretePizza
    """
    try:
        if user_pizza.get_cheese() == "":
            raise NotEnoughToppings
        else:
            print(f"Your pizza\n"
                  f"Crust: {user_pizza.get_crust()}\n"
                  f"Cheese: {user_pizza.get_cheese()}\n"
                  f"Toppings:{user_pizza.get_toppings()}\n"
                  f"Total Price: {user_pizza.get_price()}")
            print("Enter 'menu' to return to the menu or 'pay' to finish your order")
            user_input = input(">")
            if user_input == 'menu':
                return
            elif user_input == 'pay':
                print("thanks for calling Python Pizza, have a nice day.")
                time.sleep(0.5)
                sys.exit()
    except NotEnoughToppings:
        print("Sorry, your pizza must have cheese.\n")
        input("Press enter to return to the menu")
        return
if __name__ == '__main__':
    main()