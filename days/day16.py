"""--- Day 16: Chronal Classification ---"""
import re
from collections import defaultdict


def addr(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] + registers[b]
    return result


def addi(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] + b
    return result


def mulr(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] * registers[b]
    return result


def muli(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] * b
    return result


def banr(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] & registers[b]
    return result


def bani(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] & b
    return result


def borr(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] | registers[b]
    return result


def bori(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a] | b
    return result


def setr(registers, a, b, c):
    result = list(registers)
    result[c] = registers[a]
    return result


def seti(registers, a, b, c):
    result = list(registers)
    result[c] = a
    return result


def gtir(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if a > registers[b] else 0
    return result


def gtri(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if registers[a] > b else 0
    return result


def gtrr(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if registers[a] > registers[b] else 0
    return result


def eqir(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if a == registers[b] else 0
    return result


def eqri(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if registers[a] == b else 0
    return result


def eqrr(registers, a, b, c):
    result = list(registers)
    result[c] = 1 if registers[a] == registers[b] else 0
    return result


cmds = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    three_or_more_matches = 0
    for i in range(0, len(puzzle_input), 4):
        if puzzle_input[i].startswith('Before'):
            before = eval(puzzle_input[i][8:])
            instruction = list(map(int, re.findall(r'-?\d+', puzzle_input[i + 1])))
            after = eval(puzzle_input[i + 2][8:])

            matches = 0
            for cmd in cmds:
                if cmd(before, instruction[1], instruction[2], instruction[3]) == after:
                    matches += 1
            if matches >= 3:
                three_or_more_matches += 1
    return str(three_or_more_matches)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    opcode_candidates = defaultdict(set)
    last_sample_row = 0
    for i in range(0, len(puzzle_input), 4):
        if puzzle_input[i].startswith('Before'):
            before = eval(puzzle_input[i][8:])
            instruction = list(map(int, re.findall(r'-?\d+', puzzle_input[i + 1])))
            after = eval(puzzle_input[i + 2][8:])

            for cmd in cmds:
                if cmd(before, instruction[1], instruction[2], instruction[3]) == after:
                    opcode_candidates[instruction[0]].add(cmd)
            last_sample_row = i + 4
    opcodes = {}
    while len(opcodes) < len(opcode_candidates):
        for opcode, candidates in opcode_candidates.items():
            if len(candidates) == 1:
                func = candidates.pop()
                opcodes[opcode] = func
                for k in opcode_candidates.keys():
                    if func in opcode_candidates[k]:
                        opcode_candidates[k].remove(func)
    registers = [0, 0, 0, 0]
    for line in puzzle_input[last_sample_row:]:
        line = line.strip()
        if not line:
            continue
        o, a, b, c = list(map(int, re.findall(r'-?\d+', line)))
        registers = opcodes[o](registers, a, b, c)
    return str(registers[0])


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
