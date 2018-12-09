"""--- Day 09: Marble Mania ---"""
from collections import deque, defaultdict


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
    last_marble_points = int(instructions[6])

    scores = [0 for _ in range(0, players)]
    marbles = [0]
    mc = 0

    for marble_val in range(1, last_marble_points + 1):
        if marble_val % 23 == 0:
            score = marble_val
            to_remove = (mc - 7 - 1) % len(marbles) + 1
            score += marbles.pop(to_remove)
            mc = to_remove
            scores[marble_val % players - 1] += score
        else:
            place_pos = (mc + 1) % len(marbles) + 1
            mc = place_pos
            marbles.insert(place_pos, marble_val)
    return str(max(scores))


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

    scores = defaultdict(int)
    marbles = deque()
    marbles.append(0)

    for marble_val in range(1, (last_marble_point * 100 + 1)):
        if marble_val % 23 == 0:
            score = marble_val
            marbles.rotate(-7)
            score += marbles.pop()
            scores[marble_val % players - 1] += score
        else:
            marbles.rotate(2)
            marbles.append(marble_val)

    return str(max(scores.values()))


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
