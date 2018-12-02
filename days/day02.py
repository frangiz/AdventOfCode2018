"""--- Day 02: Inventory Management System ---"""
from collections import Counter
from itertools import combinations


def match(s1, s2):
    """
    Checks if two strings matches each other except for one character.

    Args:
        s1, s1 (str): String with the same length.
    Returns:
        int: The index of the character the differs.
    """
    pos = -1
    for i, (c1, c2) in enumerate(zip(s1, s2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    twos = 0
    threes = 0
    for line in puzzle_input:
        c = Counter(line)
        if len([o for o in c.most_common() if o[1] == 2]):
            twos += 1
        if len([o for o in c.most_common() if o[1] == 3]):
            threes += 1
    return str(twos * threes)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    for s1, s2 in combinations(puzzle_input, 2):
        index = match(s1, s2)
        if index != -1:
            return s1[:index] + s1[index + 1:].strip()
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
