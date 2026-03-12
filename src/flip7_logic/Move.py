from typing import List

from .Card import Card
from .Player import Player

class Move:
    def __init__(
        self,
        is_hit: bool,
        current_turn: int,
        next_turn: int,
        target_player: Player = None, # This might be setup after the move was generated
    ):
        pass