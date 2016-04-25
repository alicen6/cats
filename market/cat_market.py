from market.buy_function import egg, super_egg, legendary_egg
import sqlite3 as lite
con = lite.connect('db.sqlite3')


def cat_market(username):
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cats(
                id INTEGER PRIMARY KEY, username TEXT,
                black_cat INT, gray_cat INT, chocolate_cat INT, lilac_cat INT,
                cinnamon_cat INT, fawn_cat INT, ginger_cat INT, cream_cat INT,
                apricot_cat INT, white_cat INT, albino_cat INT, silver INT,
                brown_tabby INT, tortie INT, black_smoke INT, gray_tabby INT,
                blue_mink INT, blue_sepia INT, blue_tabby INT,
                cream_tortie INT, blue_smoke INT, blue_point INT,
                chocolate_mink INT, chocolate_sepia INT,
                lilac_tabby INT, lilac_point INT, seal_point INT,
                chocolate_tortie INT, chocolate_point INT,
                chocolate_smoke INT, lilac_cream_tortie INT, lilac_smoke INT,
                cinnamon_mink INT, cinnamon_sepia INT, cinnamon_tabby INT,
                fawn_tabby INT, cinnamon_tortie INT, cinnamon_point INT,
                cinnamon_smoke INT, fawn_mink INT, fawn_sepia INT,
                fawn_point INT, fawn_cream_tortie INT, fawn_smoke INT,
                red_tabby INT, flame_point INT, flame_mink INT, flame_sepia INT,
                cream_tabby INT, cream_point INT, cream_mink INT,
                cream_sepia INT, cameo_tabby INT, red_smoke INT,
                cream_cameo_tabby INT, cream_smoke INT, canvas_cat INT,
                silver_tabby INT, blue_silver_tabby INT, gray_lynx_point INT,
                blue_lynx_point INT, chocolate_silver_tabby INT,
                lilac_silver_tabby INT, cinnamon_silver_tabby INT,
                fawn_silver_tabby INT, red_silver_tabby INT,
                cream_silver_tabby INT, brown_lynx_point INT,
                lilac_lynx_point INT, cinnamon_lynx_point INT,
                fawn_lynx_point INT, red_lynx_point INT, cream_lynx_point INT,
                cameo_lynx_point INT, cream_cameo_lynx_point INT,
                brindled_tortie INT, brindled_cream_tortie INT,
                brindled_chocolate_tortie INT, brindled_cinnamon_tortie INT,
                brindled_lilac_tortie INT, brindled_fawn_tortie INT,
                chinchilla INT
                    );
        """)
        cur.close()
    with con:
        cur = con.cursor()
        cur.execute("""
            SELECT username FROM cats WHERE username = ?
        """, [username])
        fetch_username = cur.fetchone()
        cur.close()
    if fetch_username is None:
        with con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO cats(id, username, black_cat, gray_cat, chocolate_cat, lilac_cat,
                cinnamon_cat, fawn_cat, ginger_cat, cream_cat,
                apricot_cat, white_cat, albino_cat, silver,
                brown_tabby, tortie, black_smoke, gray_tabby,
                blue_mink, blue_sepia, blue_tabby,
                cream_tortie, blue_smoke, blue_point,
                chocolate_mink, chocolate_sepia,
                lilac_tabby, lilac_point, seal_point,
                chocolate_tortie, chocolate_point,
                chocolate_smoke, lilac_cream_tortie, lilac_smoke,
                cinnamon_mink, cinnamon_sepia, cinnamon_tabby,
                fawn_tabby, cinnamon_tortie, cinnamon_point,
                cinnamon_smoke, fawn_mink, fawn_sepia,
                fawn_point, fawn_cream_tortie, fawn_smoke,
                red_tabby, flame_point, flame_mink, flame_sepia,
                cream_tabby, cream_point, cream_mink,
                cream_sepia, cameo_tabby, red_smoke,
                cream_cameo_tabby, cream_smoke, canvas_cat,
                silver_tabby, blue_silver_tabby, gray_lynx_point,
                blue_lynx_point, chocolate_silver_tabby,
                lilac_silver_tabby, cinnamon_silver_tabby,
                fawn_silver_tabby, red_silver_tabby,
                cream_silver_tabby, brown_lynx_point,
                lilac_lynx_point, cinnamon_lynx_point,
                fawn_lynx_point, red_lynx_point, cream_lynx_point,
                cameo_lynx_point, cream_cameo_lynx_point,
                brindled_tortie, brindled_cream_tortie,
                brindled_chocolate_tortie, brindled_cinnamon_tortie,
                brindled_lilac_tortie, brindled_fawn_tortie, chinchilla) VALUES(NULL, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, [username, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0])
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
