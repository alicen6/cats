import random
import time
import sqlite3 as lite
from games.wheel_random import spin_wheel
con = lite.connect('db.sqlite3')


def wheel(username):
    print("Welcome to the Wheel of Morality!")
    print("You can spin the wheel and win wisdom")
    print("... and points!")
    print("Would you like to spin?")
    wheel_input = input("yes or no: ")
    wheel_choice = wheel_input.lower()
    if wheel_choice == "yes":
        times = 0
        print("Wheel of Morality")
        while times < 3:
            waiting()
            times += 1
        point_value, fetch_points = spin_wheel(username)
        print("You earned {0} points, and have a total of {1} points!".format(
            point_value, fetch_points))
    elif wheel_choice == "no":
        print("Okay, sending you back.")


def waiting():
    print("Turn")
    time.sleep(1)
