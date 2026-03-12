from typing import List

from .Deck import Deck
from .Deck import Deck as Discard # TODO: Make a custom class for this
from .Player import Player
from .Move import Move

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


    def generate_legal_moves(self) -> List[Move]:
        next_active_player = self.turn + 1

        while next_active_player != self.turn:
            if self.players[next_active_player].is_active:
                break

            next_active_player += 1
            next_active_player %= self.players.__len__()

        if not self.players[next_active_player].is_active:
            return []

