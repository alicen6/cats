from market.cat_market import cat_market
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def market(username):
    print("What are you looking to buy?")
    print("1. Cats, 2. Items, 3. ???")
    user_choice = int(input("pick a number: "))
    if user_choice == 1:
        cat_market(username)
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    else:
        print("That's not an option!")
