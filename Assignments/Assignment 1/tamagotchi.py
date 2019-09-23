from datetime import datetime
from edible import *
from game import *
import random


def update_check_time():
    check_time = datetime.now()
    return check_time


class Tamagotchi:
    is_dead = False
    is_sick = False

    def __init__(self, name, happiness, health, hunger):
        self.name = name
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
        if self.is_sick:
            return f"Tamagotchi status: {self.name} is sick! Name: {self.name}, " \
                   f"Hunger: {self.hunger}, Health: {self.health}, Happiness: {self.happiness}."
        else:
            return f"Tamagotchi status: Name: {self.name}, Hunger: {self.hunger}, " \
               f"Health: {self.health}, Happiness: {self.happiness}"

    def check_status(self):
        print(self)
        update_check_time()
        if self.health <= 0:
            self.is_dead = True
        if self.health <= 50:
            print(f"{self.name} is feeling a bit sick, maybe you should give him some medicine")
            self.is_sick = True
        if self.is_sick and self.health > 50:
            print(f"{self.name} feels way better after that medicine, and is no longer sick")
            self.is_sick = False


class Goku(Tamagotchi):

    def speak(self):
        if self.happiness <= 50:
            print("Goku: I can't handle being still for so long")
        elif self.hunger >= 50:
            print("Goku: Hungryyy")
        elif self.is_sick:
            print("Goku:  Think I'm getting a bit sick")
        elif self.health <= 20:
            print("Goku:  I need medicine")
        else:
            print("Goku: Power comes in response to a need, not a desire")

    def feed(self, food):
        nutrition = food.nutrition
        if food is RiceBall:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

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

    def check_status(self):
        super().check_status()
        if self.health <= 0:
            self.is_dead = True
        if self.health <= 55:
            print(f"{self.name} is feeling a bit sick, maybe you should give him some medicine")
            self.is_sick = True
        if self.is_sick and self.health > 55:
            print(f"{self.name} feels way better after that medicine, and is no longer sick")
            self.is_sick = False


class Gohan(Tamagotchi):

    def speak(self):
        if self.happiness <= 50:
            print("Gohan: We should go train!")
        elif self.hunger >= 50:
            print("Gohan: You think there's any food around here?")
        elif self.is_sick:
            print("Gohan: Ah-Choo, sorry I think I'm getting sick")
        elif self.health <= 20:
            print("Gohan:  I think I'm dying")
        else:
            print("Gohan: I know your kind. You think you can just walk in and take our planet. "
                  "But you forgot one thing...I'm my father's son!")


    def feed(self, food):
        nutrition = food.nutrition
        if food is Pudding:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

    def play(self, game):
        if game is Train:
            print("[Gohan tries to teach you how to fly]")
            self.modify_happiness(30)
        elif game is Fight:
            print("[A great threat has appeared! You fight Gohan's algebra homework with him]")
            self.modify_happiness(40)
        elif game is Spar:
            print("[You convince Gohan to spar with you]")
            self.modify_happiness(20)

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(5)
            self.modify_health(-5)
            self.modify_happiness(-10)
            iterations -= 1

    def check_status(self):
        super().check_status()
        if self.health <= 0:
            self.is_dead = True
        if self.health <= 30:
            print(f"{self.name} is feeling a bit sick, maybe you should give him some medicine")
            self.is_sick = True
        if self.is_sick and self.health > 30:
            print(f"{self.name} feels way better after that medicine, and is no longer sick")
            self.is_sick = False


class Yamcha(Tamagotchi):

    def check_status(self):
        print("Yamcha: Let go!")
        print("Piccolo: It's over")
        print("*Loud explosion*")
        self.is_dead = True


class Krillin(Tamagotchi):

    def speak(self):
        if self.happiness<= 50:
            print("Krillin: Hey, you wanna go do something?")
        elif self.hunger >= 50:
            print("Krillin: I'm really starting to get hungry!")
        elif self.is_sick:
            print("Krillin: I could use some chicken noodle soup")
        elif self.health <= 20:
            print("Krillin: I think i need to see a doctor")
        else:
            print("Krillin: Hey hun! I've got a great idea, let's trade! You take my spot and I'll fight Hercule!")

    def feed(self, food):
        nutrition = food.nutrition
        if food is SesameChicken:
            self.modify_hunger(nutrition-10)
        elif food is Medicine:
            self.modify_health(nutrition*(-1))
        else:
            self.modify_hunger(nutrition)

    def play(self, game):
        if game is Train:
            print("[Krillin tries to teach you how to throw a destructo disk]")
            self.modify_happiness(30)
        elif game is Fight:
            print("[You and Krillin watch Goku save the earth yet again]")
            self.modify_happiness(40)
        elif game is Spar:
            print("[You spar with Krillin]")
            self.modify_happiness(20)

    def update_status(self, check_time):
        new_time = datetime.now() - check_time
        iterations = new_time.seconds
        while iterations >= 1:
            self.modify_hunger(5)
            self.modify_health(-5)
            self.modify_happiness(-10)
            iterations -= 1

    def check_status(self):
        super().check_status()
        is_speak = random.randint(0, 25)
        if is_speak < 10:
            self.speak()
        if self.health <= 0:
            self.is_dead = True
        if self.health <= 30:
            print(f"{self.name} is feeling a bit sick, maybe you should give him some medicine")
            self.is_sick = True
        if self.is_sick and self.health > 30:
            print(f"{self.name} feels way better after that medicine, and is no longer sick")
            self.is_sick = False


def main():
    choice = 0
    tama = Krillin("Krillin", 100, 100, 0)
    while choice != 5:
        print("Press 1 to hatch a Tamagotchi!")
        print("Press 5 to exit")
        choice = int(input(">"))
        if choice == 1:
            tama_spinner = random.random()*100
            if 0 <= tama_spinner <= 25:
                tama = Goku(100, 100, 0)
            elif 25 < tama_spinner <= 30:
                tama = Yamcha(100, 100, 0)
            elif 30 < tama_spinner <= 60:
                tama = Krillin(100, 100, 0)
            elif 60 < tama_spinner <= 100:
                tama = Gohan(100, 100, 0)

    while choice != 5 and not tama.is_dead:
        check_time = update_check_time()
        print(f"Your {tama.name} is looking around curiously")
        print(f"")
        if choice == 2:
            tama.update_status(check_time)
            tama.check_status()
        elif choice == 3:
            tama.play(Spar)
            tama.update_status(check_time)
            tama.check_status()


if __name__ == '__main__':
    main()
