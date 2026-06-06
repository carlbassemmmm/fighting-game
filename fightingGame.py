import time
import random


def print_pause(story):
    """Prints text with a short pause."""
    print(story)
    time.sleep(1.5)


score_wins = 0


def gloves():
    attack_power = random.randrange(1, 8)
    opponents = random.randrange(1, 9)

    print_pause("You are given a mystery amount of energy.")
    print_pause("You enter the fighting arena.")
    print_pause("You encounter " + str(opponents) + " opponent(s).")
    print_pause(
        "You use your " + str(attack_power) + " attack point(s)."
    )

    if opponents > attack_power:
        print_pause("You ran out of energy!")
        print_pause("Your opponents defeated you!")
        print_pause("GAME OVER")
    else:
        print_pause("You defeated all your opponents!")
        print_pause("YOU WIN THE MATCH!")
        global score_wins
        score_wins += opponents


def sword():
    attack_power = random.randrange(1, 17)
    opponents = random.randrange(1, 17)

    print_pause("You are given a mystery amount of energy.")
    print_pause("You enter the fighting arena.")
    print_pause("You encounter " + str(opponents) + " opponent(s).")
    print_pause(
        "You use your " + str(attack_power) + " attack point(s)."
    )

    if opponents > attack_power:
        print_pause("You ran out of energy!")
        print_pause("Your opponents defeated you!")
        print_pause("GAME OVER")
    else:
        print_pause("You defeated all your opponents!")
        print_pause("YOU WIN THE MATCH!")
        global score_wins
        score_wins += opponents


def weaponselect():
    ready = input("Are you ready to begin? 1.Yes 2.No:\n")

    while ready == "1":
        while True:
            print_pause("Welcome to the Grand Fighting Tournament!")
            print_pause(
                "You must defeat opponents to become the champion."
            )
            print_pause(
                "You enter the arena and prepare for battle."
            )
            print_pause("You see two weapons.")

            selectweapon = input(
                "Choose your weapon 1.Gloves 2.Sword:\n"
            )

            while selectweapon != "1" and selectweapon != "2":
                print("Please enter a valid input.")
                selectweapon = input(
                    "Choose your weapon 1.Gloves 2.Sword:\n"
                )

            if selectweapon == "1":
                gloves()
            else:
                sword()

            playagain = input(
                "Do you wish to play again? 1.Yes 2.No:\n"
            )

            if playagain == "2":
                print_pause(
                    "You won against "
                    + str(score_wins)
                    + " opponent(s)."
                )
                return

    while ready != "1" and ready != "2":
        print("Please enter a valid input.")
        ready = input("Are you ready to begin? 1.Yes 2.No:\n")

    if ready == "2":
        print("Goodbye!")


weaponselect()