from typing import List

from .Card import Card
from .Deck import Deck
from .Deck import Deck as Discard # TODO: Make a custom class for this
from .Player import Player
from .Move import MoveDecision, MoveCardPull, MoveTargetSelection

class State:
    def __init__(
            self,
            deck: Deck,
            players: List[Player],
            discard: Discard,
            turn: int,

            points_threshold=200,
        ):

        # All info about cards and turns
        self.deck = deck
        self.players = players
        self.discard = discard
        self.turn = turn
        self.action_card = Card('f3')

        # All info about the type of move to be played
        self.is_decision = True
        self.is_card_pull = False
        self.is_target_selection = False

        # All info about round and game finish
        self.is_round_finished = False
        self.is_game_finished = False

        # Rules
        self.points_threshold = points_threshold


    def next_player_index(self):
        next_active_player = self.turn + 1

        while next_active_player != self.turn:
            if self.players[next_active_player].is_active:
                break

            next_active_player += 1
            next_active_player %= self.players.__len__()

        return next_active_player


    def generate_legal_moves(self) -> List[MoveDecision | MoveCardPull | MoveTargetSelection]:
        if self.is_round_finished:
            return []

        if self.is_decision:
            return [
                MoveDecision(
                    player=self.players[self.turn],
                    hit=False,
                ),
                MoveDecision(
                    player=self.players[self.turn],
                    hit=True,
                )
            ]

        if self.is_card_pull:
            return [
                MoveCardPull(
                    player=self.players[self.turn],
                    card=card,
                ) for card in self.deck
            ]

        if self.is_decision:
            return [
                MoveTargetSelection(
                    target_player=player,
                    card=self.action_card,
                ) for player in filter(lambda p: p.is_active, self.players)
            ]

        return []

    def make_move(self, move: MoveDecision|MoveCardPull|MoveTargetSelection):
        if isinstance(move, MoveDecision) and self.is_decision:
            pass

        if isinstance(move, MoveCardPull) and self.is_card_pull:
            pass

        if isinstance(move, MoveTargetSelection) and self.is_target_selection:
            pass