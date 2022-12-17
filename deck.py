# create a Deck class that initializes with a list of cards
class Deck():
  def __init__(self, cards):
    self.cards = []

# write a function that counts the number of cards in the deck 
  def count(self):
    len(self.cards)

# write a function that adds a card to the list of cards 
  def add_cards(self, card):
    return self.cards.append(card)

# write a function that returns the number of cards in a certain category
# not sure about this last one:
  def category_total(self, category):
    self.category = category 
    return len(category)