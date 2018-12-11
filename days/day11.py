"""--- Day 11: Chronal Charge ---"""
import helpers


def calc_power_level(x, y, serial_number):
    rack_id = x + 10
    power_lvl = (rack_id * y + serial_number) * rack_id
    return (int(power_lvl / 100) % 10) - 5


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    serial_number = int(''.join(puzzle_input))
    power_level_cache = {}
    max_xy = (-1, -1)
    max_power = -1
    for x in range(1, 300):
        for y in range(1, 300):
            sum_power = 0
            for x2 in range(x, x + 3):
                for y2 in range(y, y + 3):
                    if (x2, y2) not in power_level_cache:
                        power_level_cache[(x2, y2)] = calc_power_level(x2, y2, serial_number)
                    sum_power += power_level_cache[(x2, y2)]
            if sum_power > max_power:
                max_power = sum_power
                max_xy = (x, y)
    return str(max_xy[0]) + ',' + str(max_xy[1])


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    serial_number = int(''.join(puzzle_input))
    power_level_cache = {}
    max = (-1, -1, -1)
    max_power = -1
    for square_size in range(1, 300):
        for x in range(1, 300 - square_size):
            for y in range(1, 300 - square_size):
                sum_power = 0
                for x2 in range(x, x + square_size):
                    for y2 in range(y, y + square_size):
                        if (x2, y2) not in power_level_cache:
                            power_level_cache[(x2, y2)] = calc_power_level(x2, y2, serial_number)
                        sum_power += power_level_cache[(x2, y2)]
                if sum_power > max_power:
                    max_power = sum_power
                    max = (x, y, square_size)
                    print(max)
        print(square_size)
    return str(max[0]) + ',' + str(max[1]) + ',' + str(max[2])


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
