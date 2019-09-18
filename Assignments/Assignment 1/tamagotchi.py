from datetime import datetime
import time
class Tamagotchi:
    def __init__(self, happiness, health, hunger):
        self.happiness = happiness
        self.health = health
        self.hunger = hunger

    def raisehunger(self):
        starttime = time.time()
        while True:
            self.hunger += 1
            time.sleep(60.0 - ((time.time() - starttime) % 60.0))

    def lowerhunger(self):
        self.hunger == 0

    def lowerhealth(self):
        pass

    def raisehealth(self, health):
        self.health += health

    def lowerhappiness(self):
        pass

    def raisehappiness(self, happiness):
        self.happiness += happiness

    def speak(self):
        pass

    def die(self):
        pass

    def __str__(self):
        return f"Hi I'm  and my hunger is {self.hunger}"

class Goku(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)


    def __str__(self):
        return f"Hi I'm goku and my hunger is {self.hunger}"


class Yamcha(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)

    def __str__(self):
        return f"Hi I'm yamcha and my hunger is {self.hunger}"


class Krillin(Tamagotchi):
    def __init__(self, happiness, health, hunger):
        super().__init__(100, 100, 0)

    def __str__(self):
        return f"Hi I'm Krillin and my hunger is {self.hunger}"
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