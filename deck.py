from enum import Enum
import random
from random import shuffle
from cards.card_base_class import Card
from cards.playing_card import PlayingCard, Suit, Rank


class DeckType(Enum):
   RED = "Red Deck"
   BLUE = "Blue Deck"
   YELLOW = "Yellow Deck"
   GREEN = "Green Deck"
   BLACK = "Black Deck"
   MAGIC = "Magic Deck"
   NEBULA = "Nebula Deck"
   GHOST = "Ghost Deck"
   ABANDONED = "Abandoned Deck"
   CHECKERED = "Checkered Deck"
   ZODIAC = "Zodiac Deck"
   PAINTED = "Painted Deck"
   ANAGLYPH = "Anaglyph Deck"
   PLASMA = "Plasma Deck"
   ERRATIC = "Erratic Deck"
      
class PlayingDeck():

   def __init__(self, deck_type: DeckType):
      self.deck_type = deck_type
      self.name: str = deck_type.value
      self.desc: str = deck_type.value
      self.full_deck: list[PlayingCard] = []
      self.dealed_cards: list[PlayingCard] = []
      self.hands: int = 4
      self.discards: int = 3
      self.hand_size: int = 8
      self.joker_slots: int = 5
      self.consumable_slots: int = 2
      self.money: int = 4
      self.round: int = 0
      self.ante: int = 1
      self.interest: int = 0
      self.interest_cap: int = 5
      


   def shuffle_deck(self):
      """
      Shuffles deck
      """
      shuffle(self.full_deck)

   def add_card(self, card: PlayingCard):
      """
      Adds provided PlayingCard to full deck
      """
      self.full_deck.append(card)
   
   def deal_cards(self, deal_num: int = None):
      """
      Deals cards from top of deck
      """
      if deal_num == None:
         deal_num = self.hand_size
      dealed_cards = self.full_deck[0:deal_num]
      self.dealed_cards.append(dealed_cards)
      return dealed_cards
   
   def remove_card(self, card_index: int):
      """
      Removes selected card from deck
      """
      self.full_deck.remove(card_index)

   def _clear_dealed_cards(self):
      """
      Clears dealed cards, used when deck is shuffled
      """
      self.dealed_cards = []

   def generate_deck(self):
      
      if self.deck_type == DeckType.BLACK:
         for i in range(0, 51):
            rank = random.randint(1, 13)
            suit = random.randint(1, 4)
            card = PlayingCard(Rank(rank), Suit(suit))
            self.add_card(card)
         return None

      for suit in Suit:
         for rank in Rank:
            card = PlayingCard(rank, suit)
            self.add_card(card)

      return None
      


   

   

class RedDeck(PlayingDeck):
   """
   Red Deck
   """

   def __init__(self):
      super().__init__(DeckType.RED)
      self.discards += 1
      

class BlueDeck(PlayingDeck):
   """
   Blue Deck
   """

   def __init__(self):
      super().__init__(DeckType.BLUE)
      self.hands += 1

class YellowDeck(PlayingDeck):
   """
   Blue Deck
   """

   def __init__(self):
      super().__init__(DeckType.YELLOW)
      self.money += 10

class GreenDeck(PlayingDeck):
   """
   Green Deck
   """

   def __init__(self):
      super().__init__(DeckType.GREEN)

class BlackDeck(PlayingDeck):
   """
   Black Deck
   """

   def __init__(self):
      super().__init__(DeckType.BLACK)
      self.joker_slots += 1
      self.hands -= 1

class MagicDeck(PlayingDeck):
   """
   Magic deck
   """

   def __init__(self):
      super().__init__(DeckType.MAGIC)
      
class NebulaDeck(PlayingDeck):
   """
   Nebula Deck
   """

   def __init__(self):
      super().__init__(DeckType.NEBULA)
      self.consumable_slots -= 1
