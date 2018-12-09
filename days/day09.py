"""--- Day 09: Marble Mania ---"""
from collections import deque, defaultdict


def play_marbles(players, last_marble_point):
    scores = defaultdict(int)
    marbles = deque()
    marbles.append(0)

    for marble_val in range(1, (last_marble_point + 1)):
        if marble_val % 23 == 0:
            marbles.rotate(-7)
            scores[marble_val % players - 1] += marble_val + marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(marble_val)
    return max(scores.values())


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    instructions = ''.join(puzzle_input).split()
    players = int(instructions[0])
    last_marble_point = int(instructions[6])

    max_score = play_marbles(players, last_marble_point)
    return str(max_score)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    instructions = ''.join(puzzle_input).split()
    players = int(instructions[0])
    last_marble_point = int(instructions[6])
    max_score = play_marbles(players, last_marble_point * 100)
    return str(max_score)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
