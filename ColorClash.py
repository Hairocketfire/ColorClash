import random

# Set card class 
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        return f"{self.color} {self.value}"

# Create deck
def create_deck():
    colors = ["Rot", "Blau", "Grün", "Gelb"]
    values = list(range(0, 10))  
    deck = [Card(color, value) for color in colors for value in values]
    return deck

# Shuffle the crteated Game Deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal the cards
def deal_cards(deck, num_players=2, cards_per_player=7):
    players = {}
    for i in range(num_players):
        players[f"Spieler {i+1}"] = deck[i*cards_per_player:(i+1)*cards_per_player]
    return players

# Start the game 
def start_game():
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)
    print("Spiel gestartet mit gemischtem Kartenstapel:")
    players = deal_cards(shuffled_deck)
    for player, cards in players.items():
        print(f"{player} hat folgende Karten: {cards}")

start_game()
