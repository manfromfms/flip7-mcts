# flip7-mcts
Monte Carlo Tree Search engine for the board game "Flip 7".

## Installation

Tested on Python 3.14. 

```commandline
# Make virtual environment
python -m venv .venv

# Load the venv
# Linux
source .venv/bin/activate

# Windows
# (add this command)

# Install requirements
pip install -r requirements.txt
```

## Rules

1) In the deck there are:
   1) For each `n` in 1, 2, ... , 12 there are `n` cards giving `n` points.
   2) One `0` giving `0` points
   3) Three of each action cards (can be used on any player, including yourself):
      1) Freeze - make someone of your choice pass
      2) Flip 3 - make someone of your choice flip 3 cards
      3) Second chance - keep until busting, then discard with the repeating number card. Only one SC card at once is allowed, others are given away or discarded if everyone has SC card.
   4) For each `n` in 2, 4, ... , 10 there is a score modifier card granting `+n` points to a player. This card can't make one bust.
   5) One `x2` doubling hand score at the end of the round.
2) On your turn you can `hit` getting one more card or `pass` and keep you hand score.
3) If there is ever a repeating number card in your hand you bust right away getting 0 points.
4) Round ends when all players pass or someone hits `7` number cards in total.
5) At the end of the round every passed player counts their hand score:
   1) Add all number cards
   2) Add all `+n` modifier card
   3) Double the score if you have `x2` 
6) At the end of the round when at least one player reaches `200` points, the player with the most points wins.
7) Being the only active player, you have to use all action on yourself.

## TODO

1) Full evaluation solo - `Rule 7` simplifies the game a lot. Probabilities could be calculated precisely.
2) MCTS evaluation multiplayer