"""--- Day 17: Reservoir Research ---"""
from helpers import Point
from collections import defaultdict

def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    clay = set()
    for line in puzzle_input:
        xpart, ypart = line.split(', ')
        x = int(xpart[2:])
        from_y, to_y = ypart[2:].split('..')
        for y in range(int(from_y), int(to_y) + 1):
            clay.add(Point(x, y))
    print(clay)
    water_spring = Point(500, 0)
    return str(0)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
