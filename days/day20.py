"""--- Day 20: A Regular Map ---"""
from collections import defaultdict


def traverse(puzzle_input):
    distances = defaultdict(int)
    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    branches = []
    pos = (0, 0)
    for c in ''.join(puzzle_input)[1:-1]:
        if c == '(':
            branches.append(pos)
        elif c == ')':
            pos = branches.pop()
        elif c == '|':
            pos = branches[-1]
        elif c in directions.keys():
            prev_pos = pos
            pos = tuple(map(sum, zip(pos, directions[c])))
            if distances[pos] == 0:
                distances[pos] = distances[prev_pos] + 1
            else:
                distances[pos] = min(distances[pos], distances[prev_pos])
    return distances


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    return str(max(traverse(puzzle_input).values()))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(sum(1 for r in traverse(puzzle_input).values() if r >= 1000))


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
