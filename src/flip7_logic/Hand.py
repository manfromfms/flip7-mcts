from typing import List

from .Card import Card

class Hand:
    """
    Both a list and a set of cards. Use `Deck` if the order matters.
    """
    def __init__(self, cards: List[Card]):
        self.cards = cards

        self.set = {card for card in cards if card.is_number}


    def __contains__(self, item):
        """
        Checks whether the card is already in hand.
        """
        return item in self.set


    def append(self, card: Card):
        """
        Append a card to the hand. Returns `True` if the card is not unique. Counts only number cards.
        """
        self.cards.append(card)

        existed = card in self.set and card.is_number
        self.set.add(card)

        return existed


    def pop(self, index):
        """
        Remove a card from an index. Returns `True` if the card was unique. Counts only number cards.
        """
        card = self.cards.pop(index)

        if card in self.cards or not card.is_number:
            return False

        else:
            self.set.remove(card)
            return True


    def check_full_hand(self, amount=7):
        """
        Check whether the hand is full or not. Change standard size using `amount` param.
        """
        return self.set.__len__() >= amount


    def evaluate_hand_score(self):
        is_doubled = False

        score = 0

        for card in self.cards:
            if card.is_number:
                score += card.number_value

            elif card.is_modifier_add:
                score += card.modifier_value

            elif card.is_modifier_double:
                is_doubled = True

        if is_doubled:
            score *= 2

        return score