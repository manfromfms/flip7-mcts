from __future__ import annotations

import random
from typing import List

from .Card import Card
from .Deck import Deck
from .Player import Player


class MoveDecision:
    def __init__(
            self,
            player: Player,
            hit: bool
        ):
        self.player = player
        self.hit = hit

    def __repr__(self):
        return f'MoveDecision(player={self.player}, hit={self.hit})'


class MoveCardPull:
    def __init__(
            self,
            player: Player,
            card: Card,
        ):
        self.player = player
        self.card = card

    def __repr__(self):
        return f'MoveCardPull(player={self.player}, card={self.card})'


    @staticmethod
    def FromDeckTop(player: Player, deck: Deck) -> MoveCardPull:
        return MoveCardPull(
            player=player,
            card=deck[-1],
        )


    @staticmethod
    def FromDeckRandom(player: Player, deck: Deck) -> MoveCardPull:
        return MoveCardPull(
            player=player,
            card=deck[random.randint(0, deck.__len__())],
        )


class MoveTargetSelection:
    def __init__(
            self,
            target_player: Player,
            card: Card,
        ):
        self.target_player = target_player
        self.card = card


    def __repr__(self):
        return f'MoveDecision(target_player={self.target_player}, card={self.card})'