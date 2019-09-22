import tamagotchi
import random
from datetime import datetime
class Controller:
    def __init__(self):
        print("hi")


def main():
    timers = datetime.now()
    print(timers)
    choice = int(input(("testing datetime")))
    if choice == 1:
        nippy = datetime.now() - timers
        print(nippy.seconds)

if __name__ == '__main__':
    main()