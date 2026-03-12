from .Hand import Hand

class Player:
    def __init__(self, hand: Hand, score: int, has_passed: bool):
        self.hand = hand
        self.score = score
        self.has_passed = has_passed