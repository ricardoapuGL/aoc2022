""" 
--- Day 2: Rock Paper Scissors ---
The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""
ROCK = 0
PAPER = 1
SCISSORS = 2


pick_points = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
}

WIN_POINTS = 6
DRAW_POINTS = 3
LOSE_POINTS = 0

opponent_moves_key = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

my_moves_key = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}

win_conditions = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}


total_score = 0

with open("02.txt") as input:
    for line in input:
        line = line.strip("\n")
        [opponent_move_letter, my_move_letter] = line.split(" ")
        my_move = my_moves_key[my_move_letter]
        opponent_move = opponent_moves_key[opponent_move_letter]
        print(f"my_move: {my_move} \n opponent_move: {opponent_move}")

        total_score += pick_points[my_move]
        if my_move == opponent_move:
            # Draw
            total_score += DRAW_POINTS
        elif win_conditions[my_move] == opponent_move:
            # I win
            total_score += WIN_POINTS
        else:
            # lose
            total_score += LOSE_POINTS

print("Part One Total Score: ", total_score)

result_needed_key = {
    "X": LOSE_POINTS,
    "Y": DRAW_POINTS,
    "Z": WIN_POINTS,
}

inverse_win_conditions = {v: k for k, v in win_conditions.items()}

total_score = 0
my_move = None
opponent_move = None

with open("02.txt") as input:
    for line in input:
        line = line.strip("\n")
        [opponent_move_letter, needed_result_letter] = line.split(" ")
        opponent_move = opponent_moves_key[opponent_move_letter]
        result_needed = result_needed_key[needed_result_letter]
        print(f"opponent_move: {opponent_move} \n result needed: {opponent_move}")

        if result_needed_key[needed_result_letter] == DRAW_POINTS:
            my_move = opponent_move
            total_score += DRAW_POINTS
        elif result_needed_key[needed_result_letter] == WIN_POINTS:
            my_move = inverse_win_conditions[opponent_move]
            total_score += WIN_POINTS
        else:
            my_move = win_conditions[opponent_move]
            total_score += LOSE_POINTS
        total_score += pick_points[my_move]


print("Part Two Total Score: ", total_score)
