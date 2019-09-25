from tamagotchi import *
from edible import *
from game import *


def main():
    """
    main method loops until user inputs 5. Assigns tama to a random
    Tamagotchi object. Allows user to play/feed/check tamagotchi status.
    """
    choice = 0
    tama = Tamagotchi("Tama", 100, 100, 0)
    while choice != 5:
        print("Press 1 to hatch a Tamagotchi!")
        print("Press 5 to exit")
        choice = int(input(">"))
        if choice == 1:
            tama_spinner = random.random()*100
            if 0 <= tama_spinner <= 25:
                tama = Goku("Goku", 100, 100, 0)
            elif 25 < tama_spinner <= 30:
                tama = Yamcha("Yamcha", 100, 100, 0)
            elif 30 < tama_spinner <= 60:
                tama = Krillin("Krillin", 100, 100, 0)
            elif 60 < tama_spinner <= 100:
                tama = Gohan("Gohan", 100, 100, 0)
        else:
            print("Sorry that's an invalid input")
            choice = 5
        while choice != 5 and not tama.is_dead:
            check_time = update_check_time()
            print(f"{tama.name} is looking around curiously")
            print(f"1. play with {tama.name}")
            print(f"2. feed or give {tama.name} Medicine")
            print(f"3. to check {tama.name}'s status")
            print(f"5. Quit")
            choice = int(input(">"))
            if choice == 1:
                activity_choice = 0
                print(f"1. Fight evil with {tama.name}")
                print(f"2. Train with {tama.name}")
                print(f"3. Spar with {tama.name}")
                activity_choice = int(input(">"))
                if activity_choice == 1:
                    tama.play(Fight)
                    activity_choice = 0
                elif activity_choice == 2:
                    tama.play(Train)
                    activity_choice = 0
                elif activity_choice == 3:
                    tama.play(Spar)
                    activity_choice = 0

            elif choice == 2:
                print(f"1. Feed {tama.name} a rice ball")
                print(f"2. Feed {tama.name} pudding")
                print(f"3. Feed {tama.name} sushi")
                print(f"4. Give {tama.name} medicine")
                activity_choice = int(input(">"))
                if activity_choice == 1:
                    tama.feed(RiceBall)
                    activity_choice = 0
                elif activity_choice == 2:
                    tama.feed(Pudding)
                    activity_choice = 0
                elif activity_choice == 3:
                    tama.feed(Sushi)
                    activity_choice = 0
                elif activity_choice == 4:
                    tama.feed(Medicine)
                    activity_choice = 0

            elif choice == 3:
                tama.check_status()
                tama.update_status(check_time)
            elif choice == 5:
                print("Please play again!")
            else:
                print("Sorry that's an invalid input")


if __name__ == '__main__':
    main()