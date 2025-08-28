from dataclasses import dataclass
from enum import Enum
from cards.card_base_class import Card, CardType


class ConsumableType(Enum):
    TAROT = "Tarot"
    SPECTRAL = "Spectral"
    PLANET = "Planet"


class TarotType(Enum):
    FOOL = "The Fool"
    MAGICIAN = "The Magician"
    PREISTESS = "The High Priestess"
    EMPRESS = "The Empress"
    EMPEROR = "The Emperor"
    HIEROPHANT = "The Hierophant"
    LOVERS = "The Lovers"
    CHARIOT = "The Chariot"
    JUSTICE = "Justice"
    HERMIT = "The Hermit"
    WHEEL = "The Wheel of Fortune"
    STRENGTH = "Strength"
    HANGED = "The Hanged Man"
    DEATH = "Death"
    TEMPERANCE = "Temperance"
    DEVIL = "The Devil"
    TOWER = "The Tower"
    STAR = "The Star"
    MOON = "The Moon"
    SUN = "The Sun"
    JUDGEMENT = "Judgement"
    WORLD = "The World"


class Planet(Enum):
    MERCURY = "Mercury"
    VENUS = "Venus"
    EARTH = "Earth"
    MARS = "Mars"
    JUPITER = "Jupiter"
    SATURN = "Saturn"
    URANUS = "Uranus"
    NEPTUNE = "Neptune"
    PLUTO = "Pluto"
    PLANETX = "Planet X"
    CERES = "Ceres"
    ERES = "Eres"


class SpectralType(Enum):
    FAMILIAR = "Familiar"
    GRIM = "Grim"
    INCANTATION = "Incantation"
    TALISMAN = "Talisman"
    AURA = "AURA"
    WRATH = "Wrath"
    SIGIL = "Sigil"
    OUIJA = "Ouija"
    ECTOPLASM = "Ectoplasm"
    IMMOLATE = "Immolate"
    ANKH = "Ankh"
    DEJAVU = "Deja Vu"
    HEX = "Hex"
    TRANCE = "Trance"
    MEDIUM = "Medium"
    CRYPTID = "Cryptid"
    SOUL = "Soul"
    BLACKHOLE = "Black Hole"


class Consumable(Card):
    """
    Generic consumable class
    """

    def __init__(self, type: ConsumableType):
        super().__init__(CardType.CONSUMABLE)
        self.type = type
        self._ready = True


class TarotCard(Consumable):
    """
    TarotCard class
    """

    def __init__(self, tarot_type: TarotType):
        super().__init__(ConsumableType.TAROT)
        self.tarot_type = tarot_type
        self.name: str = self.tarot_type.value
        self.desc: str = self.tarot_type.value


class PlanetCard(Consumable):
    """
    TarotCard class
    """

    def __init__(self, planet: Planet):
        super().__init__(ConsumableType.PLANET)
        self.planet = planet
        self.name: str = self.planet.value
        self.desc: str = self.planet.value
        effect: callable = None


class SpectralCard(Consumable):

    def __init__(self, spectral_type: SpectralType):
        super().__init__(ConsumableType.SPECTRAL)
        self.spectral_type = spectral_type
        self.name: str = self.spectral_type.value
        self.desc: str = self.spectral_type.value
        effect: callable = None
