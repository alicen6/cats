suits = {
    "spade": "\u2660",
    "diamond": "\u2666",
    "heart": "\u2665",
    "club": "\u2663"
}

faces = {
    "1": "A",
    "11": "J",
    "12": "Q",
    "13": "K"
}


def draw_card(suit, value):
    icon = suits[suit]
    try:
        if (int(value) > 1 and int(value) < 11):
            if int(value) != 10:
                value = str(value) + " "
        else:
            value = faces[str(value)] + " "
    except Exception as error:
        value = value + " "
        print(error)
    drawn_card = "|{0}{1}|".format(value, icon)
    # print(drawn_card)
    return drawn_card


if __name__ == "__main__":
    values = [str(x) for x in list(range(1, 14))]
    for value in values:
        for suit in suits:
            draw_card(suit, value)
