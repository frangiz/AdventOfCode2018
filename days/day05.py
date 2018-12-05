"""--- Day 05: Alchemical Reduction ---"""
import string


def compress(result):
    last_len = len(result)
    while True:
        new_result = []
        index = 0
        while index < len(result) - 1:
            c1 = ord(result[index])
            c2 = ord(result[index + 1])
            if abs(c1 - c2) == 32:
                index += 2
            else:
                new_result.append(chr(c1))
                index += 1
        if index == len(result) - 1:
            new_result.append(result[index])
        result = ''.join(new_result)
        if len(result) == last_len:
            break
        last_len = len(result)
    return len(result)


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    result = ''.join(puzzle_input)
    
    return str(compress(result))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    result = ''.join(puzzle_input)
    min_len = 10000000000
    for c in string.ascii_lowercase:
        new_polymer = result.replace(c, '').replace(chr(ord(c) - 32), '')
        len_compressed = compress(new_polymer)
        if len_compressed < min_len:
            min_len = min(min_len, len_compressed)
    return str(min_len)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
