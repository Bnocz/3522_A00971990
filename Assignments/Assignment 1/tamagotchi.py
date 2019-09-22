from datetime import datetime
from edible import *
from game import *


class Tamagotchi:
    is_dead = False
    is_sick = False
    def __init__(self, happiness, health, hunger):
        self.happiness = happiness
        self.health = health
        self.hunger = hunger

    def modify_hunger(self, hunger):
        if self.hunger >= 100:
            self.hunger = 100
        elif self.hunger < 0:
            self.hunger = 0
        else:
            self.hunger += hunger

    def modify_health(self, health):
        if self.health < 0:
            self.health = 0
        elif self.hunger >= 100 and health < 0:
            self.health += health*2
        elif self.health > 100:
            self.health = 100
        else:
            self.health += health

    def modify_happiness(self, happiness):
        if self.happiness < 0:
            self.happiness = 0
        elif self.happiness < 0:
            self.happiness = 0
        elif self.happiness > 100:
            self.happiness = 100
        else:
            self.happiness += happiness

    def speak(self):
        print("I'm a tamagotchi")

    def die(self):
        pass

    def feed(self, food):
        self.hunger -= food.nutrition

    def play(self, game):
        if game is Train:
            pass
        if game is Fight:
            pass
        if game is Spar:
            pass

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(1)
            self.modify_health(1)
            self.modify_happiness(1)
            iterations -= 1

    def __str__(self):
        return f"Hi I'm  and my hunger is {self.hunger}"

    def check_status(self):
        print(self)
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
        return f"Hi I'm goku, my hunger is {self.hunger}, health is {self.health}, and happiness is {self.happiness}"

    def feed(self, food):
        nutrition = food.nutrition
        if food is RiceBall:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

    def check_status(self):
        super().check_status()
        if self.health <= 0:
            self.is_dead = True
        if self.health <= 50:
            print("Goku is feeling a bit sick, maybe you should give him some medicine")
            self.is_sick = True
        if self.is_sick and self.health > 50:
            print("Goku feels way better after that medicine, and is no longer sick")
            self.is_sick = False


    def play(self, game):
        if game is Train:
            print("[Goku puts on his weighted clothing and takes you for a run]")
            self.modify_happiness(30)
        elif game is Fight:
            print("[Another threat to earth has appeared! You, and Goku fight it]")
            self.modify_happiness(40)
        elif game is Spar:
            print("[Goku spars with you!]")
            self.modify_happiness(20)

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(15)
            self.modify_health(-10)
            self.modify_happiness(-5)
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

    def feed(self, food):
        nutrition = food.nutrition
        if food is Pudding:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

    def check_status(self):
        super().check_status()

    def is_sick(self):
        if self.health <= 30:
            return True

    def play(self, game):
        if game is Train:
            print("[Gohan shows you how he trained with Piccolo]")
            self.modify_happiness(30)
        elif game is Fight:
            print("[An epic battle has begun between Gohan, and his algebra homework. You decide to help out.]")
            self.modify_happiness(40)
        elif game is Spar:
            print("[Gohan decides to get some exercise, you spar with each other.]")
            self.modify_happiness(20)

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(5)
            self.modify_health(10)
            self.modify_happiness(10)
            iterations -= 1



class Yamcha(Tamagotchi):

    def __str__(self):
        return f"Hi I'm yamcha and my hunger is {self.hunger}"


class Krillin(Tamagotchi):

    def __str__(self):
        return f"Hi I'm Krillin and my hunger is {self.hunger}"

    def feed(self, food):
        nutrition = food.nutrition
        if food is SesameChicken:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

    def is_sick(self):
        if self.health <= 30:
            return True

    def play(self, game):
        if game is Train:
            print("[Krillin ]")
            self.modify_happiness(30)
        elif game is Fight:
            print("[Another threat to earth has appeared! You, and Goku fight it]")
            self.modify_happiness(40)
        elif game is Spar:
            print("[Goku spars with you!]")
            self.modify_happiness(20)

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(10)
            self.modify_health(20)
            self.modify_happiness(20)
            iterations -= 1




def main():

    tama = Goku(100, 100, 0)
    choice = 0

    while choice != 1:
        print("we testin")
        choice = int(input("fade me fam"))
        while choice != 1 and not tama.is_dead:
            check_time = tama.update_check_time()
            choice = int(input("press 2 to feed your tamagotchi"))
            if choice == 2:
                tama.feed(Medicine)
                tama.update_status(check_time)
                tama.check_status()
            elif choice == 3:
                tama.play(Spar)
                tama.update_status(check_time)
                tama.check_status()




if __name__ == '__main__':
    main()