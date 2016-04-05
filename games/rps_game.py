import random
from games.rps_logic import rps_logic
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def rps(username):
    print("Rock, Paper, Scissors is a betting game.")
    print("How much do you want to bet?")
    user_bet = int(input("pick a number: "))
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT points from users WHERE username = ?
        """, [username])
        fetch_points = cur.fetchone()[0]
        if fetch_points > user_bet:
            multiplier = rps_logic()
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
