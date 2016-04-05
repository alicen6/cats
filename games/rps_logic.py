import random
import time


def rps_logic():
    multiplier = 0
    print("Make your choice.")
    user_choice = int(input("1. rock, 2. paper or 3. scissors?: "))
    dealer_choice = random.randint(1,3)
    print("Roh!")
    time.sleep(1)
    print("Sham!")
    time.sleep(1)
    print("Bo!")
    time.sleep(1)
    if user_choice == 1:
        if dealer_choice == 1:
            print("Dealer's choice: rock")
            print("Player's choice: rock")
            print("It's a tie!")
            multiplier = 0
        elif dealer_choice == 2:
            print("Dealer's choice: paper")
            print("Player's choice: rock")
            print("Dealer wins!")
            multiplier = -1
        else:
            print("Dealer's choice: scissors")
            print("Player's choice: rock")
            print("You win!")
            multiplier = 2
    elif user_choice == 2:
        if dealer_choice == 1:
            print("Dealer's choice: rock")
            print("Player's choice: paper")
            print("You win!")
            multiplier = 2
        elif dealer_choice == 2:
            print("Dealer's choice: paper")
            print("Player's choice: paper")
            print("It's a tie!")
            multiplier = 0
        else:
            print("Dealer's choice: scissors")
            print("Player's choice: paper")
            print("Dealer wins!")
            multiplier = -1
    elif user_choice == 3:
        if dealer_choice == 1:
            print("Dealer's choice: scissors")
            print("Player's choice: rock")
            print("Dealer wins!")
            multiplier = -1
        elif dealer_choice == 2:
            print("Dealer's choice: paper")
            print("Player's choice: scissors")
            print("You win!")
            multiplier = 2
        else:
            print("Dealer's choice: scissors")
            print("Player's choice: scissors")
            print("It's a tie!")
            multiplier = 0
    else:
        print("You tried to cheat, you lose!")
        multiplier = -1
    return multiplier
