from .Hand import Hand

class Player:
    def __init__(self, hand: Hand, score: int, is_active: bool):
        self.hand = hand
        self.score = score
        self.is_active = is_active


    def __repr__(self):
        return f'Player(hand={self.hand}, score={self.score}, is_active={self.is_active})'