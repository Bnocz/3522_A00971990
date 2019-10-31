from pizzashop import *
def main():
    myPizza = ConcretePizza()
    myPizza = Pepperoni(myPizza)
    myPizza = Mozarella(myPizza)
    myPizza = Peppers(myPizza)
    print(f'Crust: {myPizza.get_crust()}\n'
          f''
          f'Toppings: {myPizza.get_cheese()} {myPizza.get_toppings()}\nPrice: {myPizza.get_price()}')


if __name__ == '__main__':
    main()