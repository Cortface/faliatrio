from enum import Enum
from cards.card_effects import Seal, Edition, Enhancement
from cards.card_base_class import Card, CardType


class Suit(Enum):
    HEARTS = "Hearts"
    CLUBS = "Clubs"
    SPADES = "Spades"
    DIAMONDS = "Diamonds"


class Rank(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"


class PlayState(Enum):
    HAND = "In Hand"
    PLAYED = "Played"
    DISCARDED = "Discarded"
    DECK = "In Deck"
    DESTROYED = "Destroyed"
    SELECTED = "Selected"


class PlayingCard(Card):
    """
    Playing Card class
    """

    def __init__(self, rank: Rank = Rank.TEN, suit: Suit = Suit.HEARTS):
        super().__init__(CardType.PLAYING)
        self.rank = rank
        self.suit = suit
        self.chips: int = 10
        self.mult: int = 0
        self.name = f"{self.rank.value} of {self.suit.value}"
        self.desc = f"+{str(self.chips)}"
        self._is_face = True
        self.state: PlayState = PlayState.DECK

    def update_suit(self, suit: Suit = None):
        """
        Update card suit to provided suit
        """
        self.suit = suit

    def update_rank(self, rank: Rank = None):
        """
        Update card rank to provided rank
        """
        self.rank = rank

    def add_chips(self, chips=0):
        """
        Add more chips to base score
        """
        self.chips += chips

    def add_mult(self, mult=0):
        """
        Add more mult to base score
        """
        self.mult += mult
