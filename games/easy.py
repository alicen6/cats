import random
import time
from games.cards import draw_card
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def easy(username):
    print("Higher or Lower!")
    print("The dealer will flip one card and you")
    print("must guess whether the next card will be")
    print("higher or lower than the last!")
    point_value = 0
    suits = ['spade', 'diamond', 'heart', 'club']
    first_suit = random.choice(suits)
    first_card = random.randint(1, 13)
    print("First Card: " + draw_card(first_suit, first_card))
    user_guess = input("higher or lower?: ").lower()
    second_suit = random.choice(suits)
    second_card = random.randint(1, 13)
    if user_guess == "higher":
        if second_card > first_card:
            time.sleep(1)
            print("You win!")
            print("Second Card: " + draw_card(second_suit, second_card))
            point_value = 4
        else:
            time.sleep(1)
            print("You lose!")
            print("Second Card: " + draw_card(second_suit, second_card))
    elif user_guess == "lower":
        if second_card < first_card:
            time.sleep(1)
            print("You win!")
            print("Second Card: " + draw_card(second_suit, second_card))
            point_value = 4
        else:
            time.sleep(1)
            print("You lose!")
            print("Second Card: " + draw_card(second_suit, second_card))
    else:
        print("That wasn't an option!")
    with con:
        cur = con.cursor()
        cur.execute("""
            UPDATE users SET points = points + ? WHERE username = ?
        """, [point_value, username])
        cur.execute("""
            SELECT points FROM users WHERE username = ?
        """, [username])
        fetch_points = cur.fetchone()[0]
        cur.close()
        return point_value, fetch_points
