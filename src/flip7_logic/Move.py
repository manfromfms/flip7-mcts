from .Card import Card
from .Player import Player

class Move:
    def __init__(self, target_player: Player, card: Card, current_turn: int, next_turn: int):
        self.target_plater = target_player
        self.card = card
        self.current_turn = current_turn
        self.next_turn = next_turn