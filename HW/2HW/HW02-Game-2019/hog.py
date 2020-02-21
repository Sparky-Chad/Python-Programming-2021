"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    # Roll dice for the number of times requested by the player
    pig_out = False
    # Score Variable
    score = 0
    for i in range(0,num_rolls):
        temp = dice()       # Temp dice handling small operations
        if temp == 1:
            pig_out = True
        score = score + temp # Add to score
    # After finishing dice rolls
    if pig_out:
        # return 1 if pig_out occured
        return 1
    #otherwise return score
    return score
    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    # Handle as a case by case or else normal game
    if num_rolls == 0:
        # Return the free pig option
        return max(int(opponent_score/10), opponent_score%10)
    else:
        # Passing dice skips need to check dice amount
        return roll_dice(num_rolls, dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    sc0 = f"{score0}"
    sc1 = f"{score1}"
    if len(sc0) < 2:
        sc0 = '0' + sc0
    if len(sc1) < 2:
        sc1 = '0' + sc1

    
    if (sc0[len(sc0)-1] + sc0[len(sc0) - 2]) == (sc1[len(sc1)-2] + sc1[len(sc1)-1]):
        return True
    return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        # Begin a game

        # Select the dice for this turn
        dice_current = select_dice(score0, score1)

        # Begin official turn
        num_dice = 0
        if who == 0:
            num_dice = strategy0(score0, score1)
            score0 += take_turn(num_dice, score1, dice=dice_current)
        else:
            num_dice = strategy1(score1, score0)
            score1 += take_turn(num_dice, score0, dice_current)        

        # Swap condition
        if is_swap(score0, score1):
            temp = score0
            score0 = score1
            score1 = temp
        
        if who == 0:
            who = 1
        else:
            who = 0
    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    # This is a really neat way to return a customized function
    def strategy(score, opponent_score):
        return n
    return strategy
