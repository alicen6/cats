import random
import time
from games.cards import draw_card
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def hard(username):
    print("Guess the Suit")
    print("The dealer will flip one card,")
    print("you will guess the suit of the next card!")
    point_value = 0
    suits = ['spade', 'diamond', 'heart', 'club']
    first_suit = random.choice(suits)
    first_card = random.randint(1, 13)
    print("First Card: " + draw_card(first_suit, first_card))
    user_guess = input("spade, heart, club or diamond?: ").lower()
    second_suit = random.choice(suits)
    second_card = random.randint(1, 13)
    if "s" in user_guess:
        if second_suit == "spade":
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You win!")
            point_value = 16
        else:
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You lose!")
            point_value = 0
    elif "d" in user_guess:
        if second_suit == "diamond":
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You win!")
            point_value = 16
        else:
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You lose!")
            point_value = 0
    elif "c" in user_guess:
        if second_suit == "club":
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You win!")
            point_value = 16
        else:
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You lose!")
            point_value = 0
    elif "h" in user_guess:
        if second_suit == "heart":
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You win!")
            point_value = 16
        else:
            time.sleep(1)
            print("Second Card: " + draw_card(second_suit, second_card))
            print("You lose!")
            point_value = 0
    else:
        "That's not an option!"
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
