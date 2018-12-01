"""--- Day 01: Chronal Calibration ---"""
import helpers
from itertools import cycle


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    return str(sum(helpers.to_ints(puzzle_input)))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    visited = set()
    freq = 0
    visited.add(freq)
    changes = helpers.to_ints(puzzle_input)
    for change in cycle(changes):
        freq += change
        if freq in visited:
            return str(freq)
        visited.add(freq)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
