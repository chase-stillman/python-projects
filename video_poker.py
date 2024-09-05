import random
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

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
def find_hole_cards():
    cards = set()
    while len(cards) < 2:
        card_val = random.choice(values)
        card_suit = random.choice(suits)
        card = card_name(card_val, card_suit)
        cards.add(card)
    return tuple(cards)

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
def main():
    print("Welcome to Python Video Poker!")
    hole_cards = find_hole_cards()
    print("Hole Cards:", hole_cards)
    board_cards = find_board_cards(hole_cards)
    print("Board Cards:", board_cards)

if __name__ == "__main__":
    main()