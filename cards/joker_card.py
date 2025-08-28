from enum import Enum
from cards.card_base_class import Card, CardType

class Joker(Enum):
    JOKER = "Joker"

class JokerCard(Card):
    """
    Joker Card class
    """

    def __init__(self, joker: Joker):
        super().__init__(CardType.JOKER)
        self.joker = joker
        self.name = joker.value
        self.desc = joker.value
        self.effect: callable = None

