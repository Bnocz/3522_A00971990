import tamagotchi
import random
class Controller:
    tama = None
    if tama is None:
        print("Press 1 to hatch a Z-Fighter")
        print("Press 0 to end")
        choice = int(input("What do you want to do? "))
        if choice == 1:
            tamagotchispawner = random.randint(1, 3)
            if tamagotchispawner == 1:
                tama = tamagotchi.Goku(100, 100, 0)
            if tamagotchispawner == 2:
                tama = tamagotchi.Yamcha(100, 100, 0)
            if tamagotchispawner == 3:
                tama = tamagotchi.Krillin(100, 100, 0)
            while True:
                print(tama)
                choice = int(input("What do you want to do? "))
                if choice == 0:
                    break;
