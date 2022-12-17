# create a Card class that intializes with a question, answer, category
class Card():
  def __init__(self, question, answer, category):
    self.question = question 
    self.answer = answer 
    self.category = category 

# create a Turn class that initialized with string representing a guess to a card’s question. The second argument is a Card object representing the current flashcard being shown


class Turn(Card):
  pass
# card = Card("What is the tallest Mountain on Earth?", "Everest", "Geography")

# print(card.question)
# print(card.answer)
# print(card.category)