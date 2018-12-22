"""--- Day 22: Mode Maze ---"""
from functools import lru_cache
from heapq import heappop, heappush


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    depth = int(puzzle_input[0].split()[1])
    x, y = puzzle_input[1].split()[1].split(',')
    target_x = int(x)
    target_y = int(y)

    @lru_cache(None)
    def erosion_level(x, y):
        if x == 0 and y == 0:
            return 0
        if x == target_x and y == target_y:
            return 0
        if y == 0:
            return ((x * 16807) + depth) % 20183
        if x == 0:
            return ((y * 48271) + depth) % 20183
        geo_idx = erosion_level(x - 1, y) * erosion_level(x, y - 1)
        return (geo_idx + depth) % 20183

    def risk(x, y):
        return erosion_level(x, y) % 3

    return str(sum(risk(x, y) for x in range(target_x + 1) for y in range(target_y + 1)))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    depth = int(puzzle_input[0].split()[1])
    x, y = puzzle_input[1].split()[1].split(',')
    target_x = int(x)
    target_y = int(y)

    @lru_cache(None)
    def erosion_level(x, y):
        if x == 0 and y == 0:
            return 0
        if x == target_x and y == target_y:
            return 0
        if y == 0:
            return ((x * 16807) + depth) % 20183
        if x == 0:
            return ((y * 48271) + depth) % 20183
        geo_idx = erosion_level(x - 1, y) * erosion_level(x, y - 1)
        return (geo_idx + depth) % 20183

    def risk(x, y):
        return erosion_level(x, y) % 3

    # invalid_gears:
    # rocky -> neither -> 0
    # wet -> torch -> 1
    # narrow -> climbing -> 2
    queue = [(0, 0, 0, 1)]  # time, x, y, invalid_gear
    fastest = {}  # (x, y, invalid_gear) -> time
    target = (target_x, target_y, 1)
    while queue:
        time, x, y, invalid_gear = heappop(queue)
        key = (x, y, invalid_gear)
        # Check if we already got a faster way reaching this position
        if key in fastest and fastest[key] <= time:
            continue
        fastest[key] = time
        if key == target:
            return str(time)
        for i in range(3):
            # Add the other options reaching this pos with switching gears
            if i != invalid_gear and i != risk(x, y):
                heappush(queue, (time + 7, x, y, i))
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            if x + dx < 0 or y + dy < 0:
                continue
            if risk(x + dx, y + dy) == invalid_gear:
                continue
            heappush(queue, (time + 1, x + dx, y + dy, invalid_gear))
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
