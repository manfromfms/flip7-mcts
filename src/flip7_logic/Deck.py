import copy
import random
from typing import List

from .Card import Card

class Deck:
    """
    A list of cards with extra functionality. Can be used to represent any ordered. Use `Hand` to handle player hand and discard pile.
    """
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def __len__(self):
        return self.cards.__len__()

    def __getitem__(self, i):
        return self.cards.__getitem__(i)

    def __contains__(self, item: Card):
        return self.cards.__contains__(item)

    def __iter__(self):
        return self.cards.__iter__()

    def append(self, card: Card):
        self.cards.append(card)

        return self

    def pop(self, index):
        return self.cards.pop(index)

    def shuffle(self):
        random.shuffle(self.cards)

        return self

    def __repr__(self):
        output = f'Deck(length={self.cards.__len__()}, '

        for card in self.cards:
            output += card.__repr__() + ', '

        output = output[:-2]
        return output + ')'

STANDARD_DECK = Deck(
    cards=[
        Card('0'),

        Card('1'),
        Card('2'),Card('2'),
        Card('3'),Card('3'),Card('3'),
        Card('4'),Card('4'),Card('4'),Card('4'),
        Card('5'),Card('5'),Card('5'),Card('5'),Card('5'),
        Card('6'),Card('6'),Card('6'),Card('6'),Card('6'),Card('6'),
        Card('7'),Card('7'),Card('7'),Card('7'),Card('7'),Card('7'),Card('7'),
        Card('8'),Card('8'),Card('8'),Card('8'),Card('8'),Card('8'),Card('8'),Card('8'),
        Card('9'),Card('9'),Card('9'),Card('9'),Card('9'),Card('9'),Card('9'),Card('9'),Card('9'),
        Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),Card('10'),
        Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),Card('11'),
        Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),Card('12'),

        Card('+2'),Card('+4'),Card('+6'),Card('+8'),Card('+10'),Card('x2'),

        Card('f'),Card('f'),Card('f'),
        Card('f3'),Card('f3'),Card('f3'),
        Card('sc'),Card('sc'),Card('sc'),
    ]
)

STANDARD_DECK_SHUFFLED = copy.deepcopy(STANDARD_DECK).shuffle()