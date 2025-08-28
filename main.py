from cards.playing_card import PlayingCard, PlayState
from deck import PlayingDeck, DeckType
import os
from enum import Enum

POKER_HAND_BASE_SCORES = {
    "High Card": {"Chips": 5, "Mult": 1},
    "Pair": {"Chips": 10, "Mult": 2},
    "Two Pair": {"Chips": 20, "Mult": 2},
    "Three of a Kind": {"Chips": 30, "Mult": 3},
    "Straight": {"Chips": 30, "Mult": 4},
    "Flush": {"Chips": 35, "Mult": 4},
    "Full House": {"Chips": 40, "Mult": 4},
    "Four of a Kind": {"Chips": 60, "Mult": 7},
    "Straight Flush": {"Chips": 100, "Mult": 8},
    "Five of a Kind": {"Chips": 10, "Mult": 2},
    "Flush House": {"Chips": 10, "Mult": 2},
    "Flush Five": {"Chips": 10, "Mult": 2},
}


class PokerHandType(Enum):
    HIGHCARD = "High Card"
    PAIR = "Two Pair"
    TWOPAIR = "Two Pair"
    THREE = "Three of a Kind"
    STRAIGHT = "Straight"
    FLUSH = "Flush"
    HOUSE = "Full House"
    FOUR = "Four of a Kind"
    STRAIGHTFLUSH = "Straight Flush"
    FIVE = "Five of a Kind"
    FLUSHHOUSE = "Flush House"
    FLUSHFIVE = "Flush Five"


class PokerHand:

    def __init__(self, type: PokerHandType = None):
        self.type = type
        self.level = 1
        self.base_chips, self.base_mult = (
            POKER_HAND_BASE_SCORES[self.type.value]["Chips"],
            POKER_HAND_BASE_SCORES[self.type.value]["Mult"],
        )
        self._num_played = 0


def determine_hand_type(selected_cards: list[PlayingCard] = []):
    """
    Determines Poker Hand Type of provided list of playing cards (upto 5)
    """
    poker_hand = None
    if len(selected_cards) == 1:
        poker_hand = PokerHandType.HIGHCARD

    if len(selected_cards) == 2:
        if selected_cards[0].rank.value == selected_cards[1].rank.value:
            poker_hand = PokerHandType.PAIR
        else:
            poker_hand = PokerHandType.HIGHCARD

    if len(selected_cards) == 3:
        if (
            selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
        ):
            poker_hand = PokerHandType.THREE
        elif (
            selected_cards[0].rank.value == selected_cards[1].rank.value
            or selected_cards[0].rank.value == selected_cards[2].rank.value
            or selected_cards[1].rank.value == selected_cards[2].rank.value
        ):
            poker_hand = PokerHandType.PAIR
        else:
            poker_hand = PokerHandType.HIGHCARD

    if len(selected_cards) == 4:
        if (
            selected_cards[0].rank.value == selected_cards[1].rank.value
            and selected_cards[0].rank.value == selected_cards[2].rank.value
            and selected_cards[0].rank.value == selected_cards[3].rank.value
        ):
            poker_hand = PokerHandType.FOUR
        elif (
            (
                selected_cards[0].rank.value == selected_cards[1].rank.value
                and selected_cards[0].rank.value == selected_cards[2].rank.value
            )
            or (
                selected_cards[0].rank.value == selected_cards[1].rank.value
                and selected_cards[0].rank.value == selected_cards[3].rank.value
            )
            or (
                selected_cards[0].rank.value == selected_cards[2].rank.value
                and selected_cards[0].rank.value == selected_cards[3].rank.value
            )
            or (
                selected_cards[1].rank.value == selected_cards[2].rank.value
                and selected_cards[1].rank.value == selected_cards[3].rank.value
            )
        ):
            poker_hand = PokerHandType.THREE
        elif (
            (
                selected_cards[0].rank.value == selected_cards[1].rank.value
                and selected_cards[2].rank.value == selected_cards[3].rank.value
            )
            or (
                selected_cards[0].rank.value == selected_cards[2].rank.value
                and selected_cards[1].rank.value == selected_cards[3].rank.value
            )
            or (
                selected_cards[0].rank.value == selected_cards[3].rank.value
                and selected_cards[1].rank.value == selected_cards[2].rank.value
            )
        ):
            poker_hand = PokerHandType.TWOPAIR
        elif (
            selected_cards[0].rank.value == selected_cards[1].rank.value
            or selected_cards[0].rank.value == selected_cards[2].rank.value
            or selected_cards[0].rank.value == selected_cards[3].rank.value
            or selected_cards[1].rank.value == selected_cards[2].rank.value
            or selected_cards[1].rank.value == selected_cards[3].rank.value
            or selected_cards[2].rank.value == selected_cards[3].rank.value
        ):
            poker_hand = PokerHandType.PAIR
        else:
            poker_hand = PokerHandType.HIGHCARD

    if len(selected_cards) == 5:

        _is_flush = False
        _is_straight = False

        if (
            selected_cards[4].rank.value == selected_cards[3].rank.value + 1
            and selected_cards[3].rank.value == selected_cards[2].rank.value + 1
            and selected_cards[2].rank.value == selected_cards[1].rank.value + 1
            and selected_cards[1].rank.value == selected_cards[0].rank.value + 1
        ):
            _is_straight = True

        if (
            selected_cards[0].suit.value
            == selected_cards[1].suit.value
            == selected_cards[2].suit.value
            == selected_cards[3].suit.value
            == selected_cards[4].suit.value
        ):
            _is_flush = True
            if _is_straight:
                poker_hand = PokerHandType.STRAIGHTFLUSH

        if (
            selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
        ):
            _is_straight = False
            if _is_flush:
                poker_hand = PokerHandType.FLUSHFIVE
            else:
                poker_hand = PokerHandType.FIVE
        elif _is_straight:
            poker_hand = PokerHandType.STRAIGHT
        elif (
            selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
            and selected_cards[3].rank.value == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[3].rank.value
            and selected_cards[2].rank.value == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[4].rank.value
            and selected_cards[2].rank.value == selected_cards[3].rank.value
            or selected_cards[0].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            and selected_cards[1].rank.value == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[2].rank.value
            == selected_cards[4].rank.value
            and selected_cards[1].rank.value == selected_cards[3].rank.value
            or selected_cards[0].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            and selected_cards[1].rank.value == selected_cards[2].rank.value
            or selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            and selected_cards[0].rank.value == selected_cards[4].rank.value
            or selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[4].rank.value
            and selected_cards[0].rank.value == selected_cards[3].rank.value
            or selected_cards[1].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            and selected_cards[0].rank.value == selected_cards[2].rank.value
            or selected_cards[2].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            and selected_cards[0].rank.value == selected_cards[1].rank.value
        ):
            if _is_flush:
                poker_hand = PokerHandType.FLUSHHOUSE
            else:
                poker_hand = PokerHandType.HOUSE
        elif (
            selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            or selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
        ):
            poker_hand = PokerHandType.FOUR
        elif _is_flush:
            poker_hand = PokerHandType.FLUSH
        elif (
            selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[2].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[3].rank.value
            or selected_cards[0].rank.value
            == selected_cards[1].rank.value
            == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            or selected_cards[0].rank.value
            == selected_cards[2].rank.value
            == selected_cards[4].rank.value
            or selected_cards[0].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            or selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[3].rank.value
            or selected_cards[1].rank.value
            == selected_cards[2].rank.value
            == selected_cards[4].rank.value
            or selected_cards[1].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
            or selected_cards[2].rank.value
            == selected_cards[3].rank.value
            == selected_cards[4].rank.value
        ):
            poker_hand = PokerHandType.THREE
        elif (
            selected_cards[0].rank.value == selected_cards[1].rank.value
            and selected_cards[2].rank.value == selected_cards[3].rank.value
            or selected_cards[0].rank.value == selected_cards[2].rank.value
            and selected_cards[3].rank.value == selected_cards[4].rank.value
            or selected_cards[0].rank.value == selected_cards[3].rank.value
            and selected_cards[2].rank.value == selected_cards[4].rank.value
            or selected_cards[0].rank.value == selected_cards[4].rank.value
            and selected_cards[2].rank.value == selected_cards[3].rank.value
            or selected_cards[1].rank.value == selected_cards[2].rank.value
            and selected_cards[3].rank.value == selected_cards[4].rank.value
            or selected_cards[1].rank.value == selected_cards[3].rank.value
            and selected_cards[0].rank.value == selected_cards[4].rank.value
            or selected_cards[1].rank.value == selected_cards[4].rank.value
            and selected_cards[2].rank.value == selected_cards[3].rank.value
        ):
            poker_hand = PokerHandType.TWOPAIR
        elif (
            selected_cards[0].rank.value == selected_cards[1].rank.value
            or selected_cards[0].rank.value == selected_cards[2].rank.value
            or selected_cards[0].rank.value == selected_cards[3].rank.value
            or selected_cards[0].rank.value == selected_cards[4].rank.value
            or selected_cards[1].rank.value == selected_cards[2].rank.value
            or selected_cards[1].rank.value == selected_cards[3].rank.value
            or selected_cards[1].rank.value == selected_cards[4].rank.value
            or selected_cards[2].rank.value == selected_cards[3].rank.value
            or selected_cards[2].rank.value == selected_cards[4].rank.value
            or selected_cards[3].rank.value == selected_cards[4].rank.value
        ):
            poker_hand = PokerHandType.PAIR
        else:
            poker_hand = PokerHandType.HIGHCARD

    return poker_hand


if __name__ == "__main__":
    deck = PlayingDeck(DeckType.RED)

    deck.generate_deck()

    deck.shuffle_deck()
    hand = deck.deal_cards()
    selected_cards = []
    num_selected = 0

    while True:

        for dealt_card in hand:
            dealt_card.state = PlayState.HAND
            print(dealt_card.name)

        user_input = input("Select cards:")
        if user_input == "q":
            break

        selection = int(user_input)

        if hand[selection].state == PlayState.SELECTED:
            hand[selection].state = PlayState.HAND
            print(hand[selection].state)
            num_selected -= 1
        elif num_selected < 5:
            hand[selection].state = PlayState.SELECTED
            print(hand[selection].state)
            num_selected += 1

        for card in hand:
            if card.state == PlayState.SELECTED:
                selected_cards.append(card)

        print(selected_cards)
        print("============================")
        for card in selected_cards:
            print(f"{card.name}\n")
        hand_type = determine_hand_type(selected_cards)
        print(hand_type)
        print("============================")
