from typing import List

from .Deck import Deck
from .Deck import Deck as Discard # TODO: Make a custom class for this
from .Player import Player

class State:
    def __init__(
            self,
            deck: Deck,
            players: List[Player],
            discard: Discard,
            turn: int
        ):

        self.deck = deck
        self.players = players
        self.discard = discard
        self.turn = turn