"""--- Day 05: Alchemical Reduction ---"""
import string

pairs = {}
for c in string.ascii_lowercase:
    pairs[c] = c.upper()
    pairs[c.upper()] = c


def compress(input_str):
    """
    Compresses the input. If a pair is removed, it checks the newly created
    space if a new pair can be removed before advancing.

    Args:
        input_str (str): The string to compress.
    Returns:
        list: A list of chars of the compressed result.
    """
    result = ['\0']
    for c in input_str:
        if pairs[c] == result[-1]:
            result.pop()
        else:
            result.append(c)

    return result[1:]


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    result = ''.join(puzzle_input)
    return str(len(compress(result)))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    result = ''.join(puzzle_input)
    min_len = 10**7
    for c in string.ascii_lowercase:
        new_polymer = result.replace(c, '').replace(c.upper(), '')
        len_compressed = len(compress(new_polymer))
        if len_compressed < min_len:
            min_len = min(min_len, len_compressed)
    return str(min_len)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
