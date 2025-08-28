from dataclasses import dataclass
from enum import Enum, StrEnum


class EditionType(Enum):
    FOIL = ("Foil", "+50 chips")
    HOLOGRAPHIC = ("Holographic", "+10 Mult")
    POLYCHROME = ("Polychrome", "X1.5 Mult")
    NEGATIVE = ("Negative", "+1 Joker slot", "+1 consumable slot")


class SealColor(Enum):
    BLUE = (
        "Blue",
        "Creates the Planet card\n for final played poker hand\n of round if held in hand\n (Must have room)",
    )
    RED = ("Red", "Retrigger this\n card 1 time")
    PURPLE = ("Purple", "Create a Tarot card\n when discarded\n (Must have room)")
    GOLD = ("Gold", "Earn $3 when this\n card is played\n and scores")


class EnhancementType(Enum):
    BONUS = ("Bonus", "+30 extra chips")
    MULT = ("Mult", "+4 Mult")
    WILD = ("Wild", "Can be used as any suit")
    GLASS = ("Glass", "X2 Mult\n 1 in 4 change to destroy card")
    STEEL = ("Steel", "X1.5 Mult\n while this card stays in hand")
    STONE = ("Stone", "+50 Chips\n no rank or suit")
    GOLD = ("Gold", "$3 if this\n card is held in hand \n at end of round")
    LUCKY = ("Lucky", "1 in 5 chance\n for +20 Mult\n 1 in 5 change\n to win $20")


class Seal:
    """
    Generic Seal Class
    """

    def __init__(self, color: SealColor = SealColor.BLUE):
        self.color: SealColor = color
        effect: callable = None


class Enhancement:
    """
    Generic enhancement class
    """

    def __init__(self):
        self.type = EnhancementType.BONUS
        self.desc: str = ""
        self.effect: callable = None


class Edition:
    """
    Generic edition class
    """

    type: str
    desc: str = ""
    effect: callable = None
