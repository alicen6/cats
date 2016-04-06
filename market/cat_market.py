from market.buy_function import egg, super_egg, legendary_egg
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def cat_market(username):
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cats(
                id INTEGER PRIMARY KEY, username TEXT
                    );
        """)
        cur.close()
    print("What would you like to buy?")
    print("1. Egg - 100 pts")
    print("2. Super Egg - 500 pts")
    print("3. Legendary Egg - 2500 pts")
    user_input = int(input("pick a number: "))
    if user_input == 1:
        with con:
            cur = con.cursor()
            cur.execute("""
                SELECT points from users WHERE username = ?
            """, [username])
            fetch_points = cur.fetchone()[0]
            if fetch_points > 100:
                pass
            else:
                print("You don't have enough points!")
    elif user_input == 2:
        with con:
            cur = con.cursor()
            cur.execute("""
                SELECT points from users WHERE username = ?
            """, [username])
            fetch_points = cur.fetchone()[0]
            if fetch_points > 500:
                pass
            else:
                print("You don't have enough points!")
    elif user_input == 3:
        with con:
            cur = con.cursor()
            cur.execute("""
                SELECT points from users WHERE username = ?
            """, [username])
            fetch_points = cur.fetchone()[0]
            if fetch_points > 2500:
                pass
            else:
                print("You don't have enough points!")
    else:
        print("That's not an option!")
