"""--- Day 01: Chronal Calibration ---"""
import helpers


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    exp = ''
    for l in puzzle_input:
        exp += l.strip()
    return str(eval(exp))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    visited = []
    val = 0
    visited.append(0)
    while True:
        for l in puzzle_input:
            if l .startswith('+'):
                val += int(l[1:])
            elif l.startswith('-'):
                val -= int(l[1:])
            if val in visited:
                return str(val)
            visited.append(val)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
