"""--- Day 21: Chronal Conversion ---"""
from collections import defaultdict


class Device():
    def __init__(self, puzzle_input):
        self.registers = [0 for _ in range(6)]
        self.ip_register = int(puzzle_input[0].split()[1])
        self.ip = self.registers[self.ip_register]
        self.instructions = puzzle_input[1:]
        self.cmds = {
            'addr': self.addr, 'addi': self.addi, 'mulr': self.mulr, 'muli': self.muli,
            'banr': self.banr, 'bani': self.bani, 'borr': self.borr, 'bori': self.bori,
            'setr': self.setr, 'seti': self.seti, 'gtir': self.gtir, 'gtri': self.gtri,
            'gtrr': self.gtrr, 'eqir': self.eqir, 'eqri': self.eqri, 'eqrr': self.eqrr}

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        self.registers[c] = 1 if a > self.registers[b] else 0

    def gtri(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] > b else 0

    def gtrr(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] > self.registers[b] else 0

    def eqir(self, a, b, c):
        self.registers[c] = 1 if a == self.registers[b] else 0

    def eqri(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] == b else 0

    def eqrr(self, a, b, c):
        self.registers[c] = 1 if self.registers[a] == self.registers[b] else 0

    def run(self):
        while self.step():
            pass

    def step(self):
        op, a, b, c = self.instructions[self.ip].split()
        self.registers[self.ip_register] = self.ip
        self.cmds[op](int(a), int(b), int(c))
        self.ip = self.registers[self.ip_register] + 1
        return 0 <= self.ip < len(self.instructions)


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    d = Device(puzzle_input)
    # At instruction #28 we compare reg[3] with reg[0]. The result will be stored in reg[1].
    # If they are equal, we will exit the loop with the next instruction. The lowest value
    # that will break the loop is the first value in reg[3] when we do a compare the first
    # time with reg[0].
    while d.ip != 28:
        d.step()
    return str(d.registers[3])


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
