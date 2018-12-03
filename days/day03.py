"""--- Day 03: No Matter How You Slice It ---"""
from collections import namedtuple, defaultdict

claim = namedtuple('claim', 'id, left, top, width, height')


def parse(puzzle_input):
    claims = []
    for line in puzzle_input:
        id, _, pos, size = line.split()
        left, top = pos[:-1].split(',')
        width, height = size.split('x')
        claims.append(claim(id=id[1:], left=int(left), top=int(top), width=int(width), height=int(height)))
    return claims


def fabric_overlaps(claims):
    overlaps = defaultdict(int)
    for claim in claims:
        for x in range(claim.width):
            for y in range(claim.height):
                overlaps[(claim.left + x, claim.top + y)] += 1
    return overlaps


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    claims = parse(puzzle_input)
    return str(sum([1 for val in fabric_overlaps(claims).values() if val > 1]))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    claims = parse(puzzle_input)
    overlaps = fabric_overlaps(claims)

    for claim in claims:
        valid = True
        for x in range(claim.width):
            for y in range(claim.height):
                if (overlaps[(claim.left + x, claim.top + y)]) > 1:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return str(claim.id)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
