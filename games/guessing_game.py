import random
from games.easy import easy
from games.medium import medium
from games.hard import hard
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def guess(username):
    print("Welcome to the Guessing Game!")
    print("There are three difficulties for this game.")
    print("Which would you like to play?")
    print("1. easy, 2. medium, 3. hard")
    user_choice = int(input("pick a number: "))
    if user_choice == 1:
        point_value, fetch_points = easy(username)
        print("You earned {0} points, and have a total of {1} points!".format(
            point_value, fetch_points))
    elif user_choice == 2:
        point_value, fetch_points = medium(username)
        print("You earned {0} points, and have a total of {1} points!".format(
            point_value, fetch_points))
    elif user_choice == 3:
        point_value, fetch_points = hard(username)
        print("You earned {0} points, and have a total of {1} points!".format(
            point_value, fetch_points))
    else:
        print("That's not an option!")
