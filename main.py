#!/usr/bin/env python3
import sqlite3 as lite
from login import login
from games.wheel import wheel
from games.blackjack import blackjack
from games.rps_game import rps
from games.guessing_game import guess
from market.market import market
con = lite.connect('db.sqlite3')


def main(username=None, assign_user=True):
    if assign_user is True:
        username = login()
        print("Hello " + username + "!")
        make_choice(username)


def make_choice(username):
    print("What would you like to do?")
    user_input = input("play or buy?: ")
    user_choice = user_input.lower()
    if user_choice == "play":
        print("What would you like to play?")
        print("1. Wheel of Morality, 2. Rock Paper Scissors, 3. Blackjack,")
        print("4. Guessing Game")
        game_choice = input("pick a number: ")
        if game_choice == "1":
            play_wheel(username)
        elif game_choice == "3":
            play_blackjack(username)
        elif game_choice == "2":
            play_rps(username)
        elif game_choice == "4":
            play_guess(username)
        else:
            print("That is not an option, please try again.")
            make_choice(username)
    elif user_choice == "buy":
        goto_market(username)
        pass
    else:
        print("That is not an option, please try again.")
        make_choice(username)


def play_wheel(username):
    wheel(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        play_wheel(username)
    else:
        make_choice(username)


def play_blackjack(username):
    blackjack(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        play_blackjack(username)
    else:
        make_choice(username)


def play_rps(username):
    rps(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        play_rps(username)
    else:
        make_choice(username)


def play_guess(username):
    guess(username)
    print("Play again?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        play_guess(username)
    else:
        make_choice(username)


def goto_market(username):
    market(username)
    print("Buy something else?")
    again_user_input = input("yes or no?: ").lower()
    if "y" in again_user_input:
        goto_market(username)
    else:
        make_choice(username)

if __name__ == "__main__":
    main()
