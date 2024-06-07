import random
import time

cards = {
    "┌─────────┐\n│A        │\n│         │\n│    ♠    │\n│         │\n│        A│\n└─────────┘": 11,
    "┌─────────┐\n│A        │\n│         │\n│    ♥    │\n│         │\n│        A│\n└─────────┘": 11,
    "┌─────────┐\n│A        │\n│         │\n│    ♦    │\n│         │\n│        A│\n└─────────┘": 11,
    "┌─────────┐\n│A        │\n│         │\n│    ♣    │\n│         │\n│        A│\n└─────────┘": 11,
    "┌─────────┐\n│2        │\n│         │\n│    ♠    │\n│         │\n│        2│\n└─────────┘": 2,
    "┌─────────┐\n│2        │\n│         │\n│    ♥    │\n│         │\n│        2│\n└─────────┘": 2,
    "┌─────────┐\n│2        │\n│         │\n│    ♦    │\n│         │\n│        2│\n└─────────┘": 2,
    "┌─────────┐\n│2        │\n│         │\n│    ♣    │\n│         │\n│        2│\n└─────────┘": 2,
    "┌─────────┐\n│3        │\n│         │\n│    ♠    │\n│         │\n│        3│\n└─────────┘": 3,
    "┌─────────┐\n│3        │\n│         │\n│    ♥    │\n│         │\n│        3│\n└─────────┘": 3,
    "┌─────────┐\n│3        │\n│         │\n│    ♦    │\n│         │\n│        3│\n└─────────┘": 3,
    "┌─────────┐\n│3        │\n│         │\n│    ♣    │\n│         │\n│        3│\n└─────────┘": 3,
    "┌─────────┐\n│4        │\n│         │\n│    ♠    │\n│         │\n│        4│\n└─────────┘": 4,
    "┌─────────┐\n│4        │\n│         │\n│    ♥    │\n│         │\n│        4│\n└─────────┘": 4,
    "┌─────────┐\n│4        │\n│         │\n│    ♦    │\n│         │\n│        4│\n└─────────┘": 4,
    "┌─────────┐\n│4        │\n│         │\n│    ♣    │\n│         │\n│        4│\n└─────────┘": 4,
    "┌─────────┐\n│5        │\n│         │\n│    ♠    │\n│         │\n│        5│\n└─────────┘": 5,
    "┌─────────┐\n│5        │\n│         │\n│    ♥    │\n│         │\n│        5│\n└─────────┘": 5,
    "┌─────────┐\n│5        │\n│         │\n│    ♦    │\n│         │\n│        5│\n└─────────┘": 5,
    "┌─────────┐\n│5        │\n│         │\n│    ♣    │\n│         │\n│        5│\n└─────────┘": 5,
    "┌─────────┐\n│6        │\n│         │\n│    ♠    │\n│         │\n│        6│\n└─────────┘": 6,
    "┌─────────┐\n│6        │\n│         │\n│    ♥    │\n│         │\n│        6│\n└─────────┘": 6,
    "┌─────────┐\n│6        │\n│         │\n│    ♦    │\n│         │\n│        6│\n└─────────┘": 6,
    "┌─────────┐\n│6        │\n│         │\n│    ♣    │\n│         │\n│        6│\n└─────────┘": 6,
    "┌─────────┐\n│7        │\n│         │\n│    ♠    │\n│         │\n│        7│\n└─────────┘": 7,
    "┌─────────┐\n│7        │\n│         │\n│    ♥    │\n│         │\n│        7│\n└─────────┘": 7,
    "┌─────────┐\n│7        │\n│         │\n│    ♦    │\n│         │\n│        7│\n└─────────┘": 7,
    "┌─────────┐\n│7        │\n│         │\n│    ♣    │\n│         │\n│        7│\n└─────────┘": 7,
    "┌─────────┐\n│8        │\n│         │\n│    ♠    │\n│         │\n│        8│\n└─────────┘": 8,
    "┌─────────┐\n│8        │\n│         │\n│    ♥    │\n│         │\n│        8│\n└─────────┘": 8,
    "┌─────────┐\n│8        │\n│         │\n│    ♦    │\n│         │\n│        8│\n└─────────┘": 8,
    "┌─────────┐\n│8        │\n│         │\n│    ♣    │\n│         │\n│        8│\n└─────────┘": 8,
    "┌─────────┐\n│9        │\n│         │\n│    ♠    │\n│         │\n│        9│\n└─────────┘": 9,
    "┌─────────┐\n│9        │\n│         │\n│    ♥    │\n│         │\n│        9│\n└─────────┘": 9,
    "┌─────────┐\n│9        │\n│         │\n│    ♦    │\n│         │\n│        9│\n└─────────┘": 9,
    "┌─────────┐\n│9        │\n│         │\n│    ♣    │\n│         │\n│        9│\n└─────────┘": 9,
    "┌─────────┐\n│10       │\n│         │\n│    ♠    │\n│         │\n│       10│\n└─────────┘": 10,
    "┌─────────┐\n│10       │\n│         │\n│    ♥    │\n│         │\n│       10│\n└─────────┘": 10,
    "┌─────────┐\n│10       │\n│         │\n│    ♦    │\n│         │\n│       10│\n└─────────┘": 10,
    "┌─────────┐\n│10       │\n│         │\n│    ♣    │\n│         │\n│       10│\n└─────────┘": 10,
    "┌─────────┐\n│J        │\n│         │\n│    ♠    │\n│         │\n│        J│\n└─────────┘": 10,
    "┌─────────┐\n│J        │\n│         │\n│    ♥    │\n│         │\n│        J│\n└─────────┘": 10,
    "┌─────────┐\n│J        │\n│         │\n│    ♦    │\n│         │\n│        J│\n└─────────┘": 10,
    "┌─────────┐\n│J        │\n│         │\n│    ♣    │\n│         │\n│        J│\n└─────────┘": 10,
    "┌─────────┐\n|Q        │\n│         │\n│    ♠    │\n│         │\n│        Q│\n└─────────┘": 10,
    "┌─────────┐\n│Q        │\n│         │\n│    ♥    │\n│         │\n│        Q│\n└─────────┘": 10,
    "┌─────────┐\n│Q        │\n│         │\n│    ♦    │\n│         │\n│        Q│\n└─────────┘": 10,
    "┌─────────┐\n│Q        │\n│         │\n│    ♣    │\n│         │\n│        Q│\n└─────────┘": 10,
    "┌─────────┐\n│K        │\n│         │\n│    ♠    │\n│         │\n│        K│\n└─────────┘": 10,
    "┌─────────┐\n│K        │\n│         │\n│    ♥    │\n│         │\n│        K│\n└─────────┘": 10,
    "┌─────────┐\n│K        │\n│         │\n│    ♦    │\n│         │\n│        K│\n└─────────┘": 10,
    "┌─────────┐\n│K        │\n│         │\n│    ♣    │\n│         │\n│        K│\n└─────────┘": 10,
}

blankcard = "┌─────────┐\n│         │\n│         │\n│         │\n│         │\n│         │\n└─────────┘"

playercards = []

playerhand = ""

playertotal = 0

dealercards = []

dealerhand = ""

dealertotal = 0

# Shuffle the keys
keys = list(cards.keys())
random.shuffle(keys)

# Create a new dictionary with shuffled keys
shuffled_cards = {key: cards[key] for key in keys}


def player_action():
    global playercards
    global playerhand
    global playertotal
    global dealercards
    global dealerhand
    global dealertotal
    decision = input("\nYou have " + str(playertotal) + "! Do you want to hit (h) or stand (s)? ")
    if decision.lower() == "h":
        playercards.append(shuffled_cards.popitem())
        playerhand += playercards[-1][0] + "\n"
        playertotal += playercards[-1][1]
        print("Your hand:\n" + playerhand)
        time.sleep(1)
        print("Your total is now: " + str(playertotal) + "\n")
        time.sleep(0.75)
        if playertotal > 21:
            print("You have bust. Dealer wins! Game over...")
            return playertotal
        else:
            player_action()
    elif decision.lower() == "s":
        print("\nYour total is " + str(playertotal) + "\nDealer's turn:\n")
        time.sleep(0.75)
        print("Dealer shows: \n" + dealerhand)
        time.sleep(0.75)
        dealer_action()


def dealer_action():
    global playercards
    global playerhand
    global playertotal
    global dealercards
    global dealerhand
    global dealertotal
    dealertotal = 0
    for key in dealercards:
        dealertotal += key[1]
    print("\nDealer has " + str(dealertotal) + "!")
    while dealertotal < 17:
        time.sleep(1.5)
        print("\nDealer hits!\n")
        dealercards.append(shuffled_cards.popitem())
        dealerhand += dealercards[-1][0] + "\n"
        dealertotal += dealercards[-1][1]
        print("Dealer hand:\n" + dealerhand)
        time.sleep(1)
        print("Dealer now has: " + str(dealertotal))
        time.sleep(0.75)
    if dealertotal > 21:
        print("\nDealer has bust! You win!!!")
    elif dealertotal > playertotal:
        print("\nDealer has " + str(dealertotal) + ". You have " + str(playertotal) + ".\n\nDealer wins!")
    elif dealertotal < playertotal:
        print("\nDealer has " + str(dealertotal) + ". You have " + str(playertotal) + ".\n\nYou win!")
    else:
        print("You both have " + str(dealertotal) + ". Its a draw...")


def play_game():
    global playercards
    global playerhand
    global playertotal
    global dealercards
    global dealerhand
    global dealertotal
    # change player and dealer cards to an array
    playercards = []
    dealercards = []
    playercards.append(shuffled_cards.popitem())
    dealercards.append(shuffled_cards.popitem())
    playercards.append(shuffled_cards.popitem())
    dealercards.append(shuffled_cards.popitem())
    print("Dealer is showing:\n" + dealercards[0][0] + "\n" + blankcard)
    dealerhand = ""
    dealerhand += dealercards[0][0] + "\n" + dealercards[1][0] + "\n"
    playerhand = ""
    playerhand += playercards[0][0] + "\n" + playercards[1][0] + "\n"
    playertotal = 0
    for key in playercards:
        playertotal += key[1]
    print("Your hand:\n" + playerhand)
    player_action()
    again = input("\nWould you like to play again? ")
    return again


def start_game():
    choice = input("Would you like to play BlackJack? ")
    if choice.lower() == "yes" or choice.lower() == "y":
        again = play_game()
        while again.lower() == "yes" or again.lower() == "y":
            again = play_game()
        else:
            print("\nThanks for playing!!")


start_game()
