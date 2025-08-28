from dataclasses import dataclass
from enum import StrEnum
from cards.card_effects import Seal, Edition, Enhancement


class CardType(StrEnum):
    JOKER = "Joker"
    CONSUMABLE = "Consumable"
    PLAYING = "Playing"


class Card:
    """
    Card Base Class
    """

    def __init__(self, card_type, enhancement=None, edition=None, seal=None):
        self.card_type = card_type
        self.enhancement = enhancement
        self.edition = edition
        self.seal = seal
        self._is_consumable = True if CardType.CONSUMABLE else False
        self._face_up = True

    def apply_enhancement(self, enhancement: Enhancement = None):
        """
        Applies provided enhancement to card
        """
        self.enhacement = enhancement

    def apply_seal(self, seal: Seal = None):
        """
        Applies provided seal to card
        """
        self.seal = seal

    def apply_edition(self, edition: Edition = None):
        """
        Applies provided edition to card
        """
        self.edition = edition

    def remove_enhancement(self):
        """
        Applies provided enhancement to card
        """
        self.enhancement = None

    def remove_seal(self):
        """
        Applies provided seal to card
        """
        self.seal = None

    def remove_edition(self):
        """
        Applies provided edition to card
        """
        self.edition = None
