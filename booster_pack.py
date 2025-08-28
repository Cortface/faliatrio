
from dataclasses import dataclass
from enum import Enum


class BoosterPackType(Enum):
    ARCANA = "Arcana"
    SPECTRAL = "Spectral"
    STANDARD = "Standard"
    BUFFOON = "Buffoon"
    CELESTIAL = "Celestial"

class BoosterPackSize(Enum):
    REGULAR = "Regular"
    JUMBO = "Jumbo"
    MEGA = "Mega"



class BoosterPack():
    """
    Generic BoosterPack class
    """

    def __init__(self):
        type: BoosterPackType = BoosterPackType.STANDARD
        size: BoosterPackSize = BoosterPackSize.REGULAR
        cards: list = [Consumable]
        picks: int = 1
    