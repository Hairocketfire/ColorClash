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

# Start the game 
def start_game():
    deck = create_deck()
    shuffled_deck = shuffle_deck(deck)
    print("Spiel gestartet mit gemischtem Kartenstapel:")
    print(shuffled_deck[:10])  # Zeige die ersten 10 Karten des gemischten Stapels als Beispiel
    return shuffled_deck

# Spiel starten und gemischten Kartenstapel anzeigen
shuffled_deck = start_game()
shuffled_deck[:10]  # Zeige die ersten 10 Karten des gemischten Stapels als Beispiel
