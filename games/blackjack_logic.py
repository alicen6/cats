import random
from games.cards import draw_card


def deal():
    multiplier = 0
    dealer_hand = []
    dealer_hand_card_count = 0
    dealer_hand_total = 0
    player_hand = []
    player_hand_card_count = 0
    player_hand_total = 0
    while dealer_hand_card_count < 2:
        suits = ['spade', 'diamond', 'heart', 'club']
        dealer_suit = random.choice(suits)
        dealer_value = random.randint(1, 13)
        player_suit = random.choice(suits)
        player_value = random.randint(1, 13)
        dealer_hand.append(draw_card(dealer_suit, dealer_value))
        player_hand.append(draw_card(player_suit, player_value))
        dealer_hand_card_count += 1
        player_hand_card_count += 1
        if dealer_value > 10:
            dealer_hand_total += 10
        elif dealer_value == 1:
            if dealer_hand_total < 11:
                dealer_hand_total += 11
            else:
                dealer_hand_total += 1
        else:
            dealer_hand_total += dealer_value
        if player_value > 10:
            player_hand_total += 10
        elif player_value == 1:
            if player_hand_total < 11:
                player_hand_total += 11
            else:
                player_hand_total += 1
        else:
            player_hand_total += player_value
    show_dealer = dealer_hand[1]
    print("DEALER HAND: " + show_dealer)
    print("YOUR HAND: " + player_hand[0] + player_hand[1])
    if player_hand_total == 21:
        print("You win! Congratulations!")
        multiplier = 2
    elif dealer_hand_total == 21:
        print("Dealer wins!")
        print(dealer_hand[0] + dealer_hand[1])
        multiplier = -1
    elif player_hand_total > 21:
        print("You bust! Sorry!")
        multiplier = -1
    elif dealer_hand_total > 21:
        print("Dealer busts! You win!")
        print(dealer_hand[0] + dealer_hand[1])
        multiplier = 2
    else:
        print("What would you like to do?")
        choice = input("hit or stand: ").lower()
        if choice == "hit":
            player_suit = random.choice(suits)
            player_value = random.randint(1, 13)
            player_hand.append(draw_card(player_suit, player_value))
            player_hand_card_count += 1
            if player_value > 10:
                player_hand_total += 10
            elif player_value == 1:
                if player_hand_total < 11:
                    player_hand_total += 11
                else:
                    player_hand_total += 1
            else:
                player_hand_total += player_value
            print("YOUR HAND: " + player_hand[0] + player_hand[1] + player_hand[2])
            if player_hand_total > 21:
                print("You bust! Sorry!")
                multiplier = -1
            else:
                print("What would you like to do?")
                choice = input("hit or stand: ").lower()
                if choice == "hit":
                    player_suit = random.choice(suits)
                    player_value = random.randint(1, 13)
                    player_hand.append(draw_card(player_suit, player_value))
                    player_hand_card_count += 1
                    if player_value > 10:
                        player_hand_total += 10
                    elif player_value == 1:
                        if player_hand_total < 11:
                            player_hand_total += 11
                        else:
                            player_hand_total += 1
                    else:
                        player_hand_total += player_value
                    print("YOUR HAND: " + player_hand[0] + player_hand[1] + player_hand[2] + player_hand[3])
                    if player_hand_total > 21:
                        print("You bust! Sorry!")
                        multiplier = -1
                    else:
                        dealer_suit = random.choice(suits)
                        dealer_value = random.randint(1, 13)
                        dealer_hand.append(draw_card(dealer_suit, dealer_value))
                        dealer_hand_card_count += 1
                        if dealer_value > 10:
                            dealer_hand_total += 10
                        elif dealer_value == 1:
                            if dealer_hand_total < 11:
                                dealer_hand_total += 11
                            else:
                                dealer_hand_total += 1
                        else:
                            dealer_hand_total += dealer_value
                        if dealer_hand_total > 21:
                            print("Dealer busts, you win!")
                            print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                            multiplier = 2
                        elif player_hand_total > dealer_hand_total:
                            print("You win!")
                            multiplier = 2
                        elif player_hand_total == dealer_hand_total:
                            print("You tied!")
                            print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                            multiplier = 0
                        else:
                            print("Dealer wins!")
                            print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                            multiplier = -1
                else:
                    dealer_suit = random.choice(suits)
                    dealer_value = random.randint(1, 13)
                    dealer_hand.append(draw_card(dealer_suit, dealer_value))
                    dealer_hand_card_count += 1
                    if dealer_value > 10:
                        dealer_hand_total += 10
                    elif dealer_value == 1:
                        if dealer_hand_total < 11:
                            dealer_hand_total += 11
                        else:
                            dealer_hand_total += 1
                    else:
                        dealer_hand_total += dealer_value
                    if dealer_hand_total > 21:
                        print("Dealer busts, you win!")
                        print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                        multiplier = 2
                    elif player_hand_total > dealer_hand_total:
                        print("You win!")
                        multiplier = 2
                    elif player_hand_total == dealer_hand_total:
                        print("You tied!")
                        print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                        multiplier = 0
                    else:
                        print("Dealer wins!")
                        print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                        multiplier = -1
        else:
            dealer_suit = random.choice(suits)
            dealer_value = random.randint(1, 13)
            dealer_hand.append(draw_card(dealer_suit, dealer_value))
            dealer_hand_card_count += 1
            if dealer_value > 10:
                dealer_hand_total += 10
            elif dealer_value == 1:
                if dealer_hand_total < 11:
                    dealer_hand_total += 11
                else:
                    dealer_hand_total += 1
            else:
                dealer_hand_total += dealer_value
            if dealer_hand_total > 21:
                print("Dealer busts, you win!")
                print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                multiplier = 2
            elif player_hand_total > dealer_hand_total:
                print("You win!")
                multiplier = 2
            elif player_hand_total == dealer_hand_total:
                print("You tied!")
                print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                multiplier = 0
            else:
                print("Dealer wins!")
                print("DEALER HAND: " + dealer_hand[0] + dealer_hand[1] + dealer_hand[2])
                multiplier = -1
    return multiplier
