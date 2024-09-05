import random
#determinging suits and values
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

#method to change the values of higher cards to their face card counterpart upon output
def card_name(value, suit):
    if value == 11:
        return "Jack of " + suit
    elif value == 12:
        return "Queen of " + suit
    elif value == 13:
        return "King of " + suit
    elif value == 14:
        return "Ace of " + suit
    else:
        return str(value) + " of " + suit

#method to find the user 2 hole cards
def find_hole_cards():
    cards = set()
    while len(cards) < 2:
        card_val = random.choice(values)
        card_suit = random.choice(suits)
        card = card_name(card_val, card_suit)
        cards.add(card)
    return tuple(cards)

#method to find the user 5 board cards, ensuring the cards are not the same suit and value as the two in a player's hole cards, as this is impossible
def find_board_cards(hole_cards):
    hole_cards_set = set(hole_cards)
    cards = set()

    while len(cards) < 5:
        card_val = random.choice(values)
        card_suit = random.choice(suits)
        card = card_name(card_val, card_suit)
        if card not in hole_cards_set:
            cards.add(card)

    return tuple(cards)

#main function. this project is still to be completed.
def main():
    print("Welcome to Python Video Poker!")
    hole_cards = find_hole_cards()
    print("Hole Cards:", hole_cards)
    board_cards = find_board_cards(hole_cards)
    print("Board Cards:", board_cards)

if __name__ == "__main__":
    main()
