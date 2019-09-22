from datetime import datetime
import time
class Tamagotchi:
    def __init__(self, happiness, health, hunger):
        self.happiness = happiness
        self.health = health
        self.hunger = hunger

    def modify_hunger(self, hunger):
        if self.hunger >= 100:
            self.hunger = 100
        else:
            self.hunger += hunger

    def modify_health(self, health):
        if self.health <= 0:
            self.health = 0
        elif self.hunger >= 100 and health < 0:
            self.health += health*2
        else:
            self.health += health

    def modify_happiness(self, happiness):
        if self.happiness <= 0:
            self.happiness = 0
        else:
            self.happiness += happiness

    def speak(self):
        print("I'm a tamagotchi")

    def die(self):
        pass

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            Tamagotchi.modify_hunger(self, 1)
            Tamagotchi.modify_health(self, 1)
            iterations -= 1

    def __str__(self):
        return f"Hi I'm  and my hunger is {self.hunger}"

    def check_status(self):
        print(Tamagotchi.speak(self))
        Tamagotchi.update_check_time(self)

    def update_check_time(self):
        check_time = datetime.now()
        return check_time


class Goku(Tamagotchi):

    def speak(self):
        if self.happiness<= 50:
            print("I'm feeling kinda down")
        if self.happiness <= 20:
            print("...")
        if self.hunger >= 50:
            print("I'm really starting to get hungry!")
        if self.hunger >= 80:
            print("I'm dying of hunger!")
        if self.health <= 50:
            print("*sniff* my nose is stuffed")
        if self.health <= 20:
            print("I think i need to see a doctor")
        else:
            print("Wonder how Gohan is doing..")

    def __str__(self):
        return f"Hi I'm goku, my hunger is {self.hunger}, and health is {self.health}"

    def check_status(self):
        super().check_status()

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            Tamagotchi.modify_hunger(self, 15)
            Tamagotchi.modify_health(self, -10)
            iterations -= 1

class Gohan(Tamagotchi):

    def speak(self):
        if self.happiness<= 50:
            print("I'm feeling kinda down")
        if self.happiness <= 20:
            print("...")
        if self.hunger >= 50:
            print("I'm really starting to get hungry!")
        if self.hunger >= 80:
            print("I'm dying of hunger!")
        if self.health <= 50:
            print("*sniff* my nose is stuffed")
        if self.health <= 20:
            print("I think i need to see a doctor")
        else:
            print("Wonder how Gohan is doing..")

    def __str__(self):
        return f"Hi I'm goku, my hunger is {self.hunger}, and health is {self.health}"

    def check_status(self):
        super().check_status()

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            Tamagotchi.modify_hunger(self, 15)
            Tamagotchi.modify_health(self, -10)
            iterations -= 1



class Yamcha(Tamagotchi):

    def __str__(self):
        return f"Hi I'm yamcha and my hunger is {self.hunger}"


class Krillin(Tamagotchi):

    def __str__(self):
        return f"Hi I'm Krillin and my hunger is {self.hunger}"



    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            Tamagotchi.modify_hunger(self, 5)
            Tamagotchi.modify_health(self, 15)
            iterations -= 1


def main():

    tama = Goku(100, 100, 0)
    choice = 0
    while choice != 1:
        check_time = tama.update_check_time()
        choice = int(input("press 2 to check your tamagachis status"))
        if choice == 2:
            tama.update_status(check_time)
            tama.check_status()




if __name__ == '__main__':
    main()