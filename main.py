#!/usr/bin/env python3
import sqlite3 as lite
from login import login
from games.wheel import wheel
from games.blackjack import blackjack
from games.rps_game import rps
con = lite.connect('db.sqlite3')


def play_wheel(username):
    wheel(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        play_wheel(username)
    else:
        main(username=username, assign_user=False)


def play_blackjack(username):
    blackjack(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        blackjack(username)
    else:
        main(username=username, assign_user=False)


def play_rps(username):
    rps_game(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        rps_game(username)
    else:
        main(username=username, assign_user=False)


def main(username=None, assign_user=True):
    if assign_user is True:
        username = login()
        print("Hello " + username + "!")
    print("What would you like to do?")
    user_input = input("play or buy?: ")
    user_choice = user_input.lower()
    if user_choice == "play":
        print("What would you like to play?")
        print("1. wheel, 2. rock paper scissors, 3. blackjack: ")
        game_choice = input("pick a number: ")
        if game_choice == "1":
            play_wheel(username)
        elif game_choice == "3":
            play_blackjack(username)
        elif game_choice == "2":
            rps_game()
            pass
        else:
            print("That is not an option, please try again.")
            main()
    elif user_choice == "buy":
        # market()
        pass
    else:
        print("That is not an option, please try again.")
        main()

if __name__ == "__main__":
    main()
