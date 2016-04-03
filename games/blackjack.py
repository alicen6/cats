import random
from games.blackjack_logic import deal
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def blackjack(username):
    print("Welcome to Blackjack, let's play.")
    print("How much would you like to bet?")
    user_bet = int(input("pick a number: "))
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT points from users WHERE username = ?
        """, [username])
        fetch_points = cur.fetchone()[0]
        if fetch_points > user_bet:
            multiplier = deal()
            point_value = user_bet * multiplier
            cur.execute("""
                UPDATE users SET points = points + ? WHERE username = ?
            """, [point_value, username])
            cur.execute("""
                SELECT points FROM users WHERE username = ?
            """, [username])
            fetch_points = cur.fetchone()[0]
        else:
            print("You don't have enough points to bet that much!")
        cur.close()
        return point_value, fetch_points
