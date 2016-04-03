import random
import sqlite3 as lite
con = lite.connect('db.sqlite3')

wheel_options = [
    "If at first you don't succeed, blame it on your parents.",
    "Never ask what hot dogs are made of.",
    "Brush your teeth after every meal. This moral brought to you by the American Dental Association.",
    "The answer, my friend, is blowing in the wind, except in New Jersey where what's blowing in the wind smells funny.",
    "If you can't say something nice, you're probably at the Ice Capades.",
    "Elvis lives on in our hearts, in his music, and in a trailer park outside Milwaukee.",
    "You can teach an old dog new tricks, but you can't teach Madonna to act.",
    "Early to rise and early to bed makes a man healthy, but socially dead.",
    "Vote early and vote often.",
    "Possums have pouches like kangaroos.",
    "Don't eat with your mouth full.",
    "Win $5,000!",
    "Win a Free Trip to Tahiti!",
    "Do not back up. Severe tire damage.",
    "Lather, rinse, repeat.",
    "Don't be a fool, stay in school.",
    "People who live in glass houses should get dressed with the lights out.",
    "Don't spit in public.",

    "2B or not 2B, that is the pencil.",
    "Just cheer up and never ever give up hope!"
]


def spin_wheel(username):
    print("Tell us the lesson that we should learn!")
    wheel_number = str(random.randint(1, 999))
    wheel_words = random.choice(wheel_options)
    choice = "#" + wheel_number + ". " + wheel_words
    print(choice)
    point_value = random.randint(1, 10)
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
