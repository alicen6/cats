import sqlite3 as lite
con = lite.connect('db.sqlite3')


def login():
    user_input = input("Username: ")
    username = user_input.lower()
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY, username TEXT,
                    points INT );
        """)
        cur.close()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT username FROM users WHERE username = ?
        """, [username])
        fetch_username = cur.fetchone()
        cur.close()
    if fetch_username is None:
        with con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO users(id, username, points) VALUES(NULL, ?, ?);
            """, [username, 0])
            cur.close()
    return username

if __name__ == "__main__":
    login()
