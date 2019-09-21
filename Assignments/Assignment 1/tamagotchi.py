from datetime import datetime
import time
class Tamagotchi:
    def __init__(self, happiness, health, hunger):
        self.happiness = happiness
        self.health = health
        self.hunger = hunger

    def raisehunger(self):
        self.hunger = 100

    def lowerhunger(self):
        pass

    def lowerhealth(self):
        pass

    def raisehealth(self, health):
        self.health = 100

    def lowerhappiness(self):
        pass

    def raisehappiness(self, happiness):
        self.happiness = 100

    def speak(self):
        pass

    def die(self):
        pass

    def check_status(self):


    def __str__(self):
        return f"Hi I'm  and my hunger is {self.hunger}"

class Goku(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)

    def speak(self):
        if self.hapiness<= 50:
            print("I'm feeling kinda down")
        if self.happiness <= 20:
            print("...")
        if self.hunger <= 50:
            print("I'm really starting to get hungry!")
        if self.hunger <= 20:
            print("I'm dying of hunger!")
        if self.health <= 50:
            print("*sniff* my nose is stuffed")
        if self.health <= 20:
            print("I think i need to see a doctor")
        else:
            print("Wonder how Gohan is doing..")



    def __str__(self):
        return f"Hi I'm goku and my hunger is {self.hunger}"


class Yamcha(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)

    def __str__(self):
        return f"Hi I'm yamcha and my hunger is {self.hunger}"

    def speak(self):
        if self.hapiness<= 50:
            print("I'm feeling kinda down")
        if self.happiness <= 20:
            print("...")
        if self.hunger <= 50:
            print("I'm really starting to get hungry!")
        if self.hunger <= 20:
            print("I'm dying of hunger!")
        if self.health <= 50:
            print("*sniff* my nose is stuffed")
        if self.health <= 20:
            print("I think i need to see a doctor")
        else:
            print("Wonder how Gohan is doing..")

class Krillin(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)

    def __str__(self):
        return f"Hi I'm Krillin and my hunger is {self.hunger}"

    def speak(self):
        if self.hapiness <= 50:
            print("I'm feeling kinda down")
        if self.happiness <= 20:
            print("...")
        if self.hunger <= 50:
            print("I'm really starting to get hungry!")
        if self.hunger <= 20:
            print("I'm dying of hunger!")
        if self.health <= 50:
            print("*sniff* my nose is stuffed")
        if self.health <= 20:
            print("I think i need to see a doctor")
        else:
            print("Wonder how Gohan is doing..")


def main():

    n = int(input("enter a number"))
    if n == 1:
        tama = Goku(100, 100, 0)
    if n == 2:
        tama = Yamcha(100, 100, 0)
    while True:
        print(tama)
        x = int(input("press 0 to end"))
        time.sleep(5)
        if x == 0:
            break



if __name__ == '__main__':
    main()