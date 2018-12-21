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
        lines_executed = defaultdict(int)
        counter = 0
        while 0 <= self.ip < len(self.instructions):
            op, a, b, c = self.instructions[self.ip].split()
            self.registers[self.ip_register] = self.ip
            self.cmds[op](int(a), int(b), int(c))
            self.ip = self.registers[self.ip_register] + 1
            lines_executed[self.ip] += 1
            counter += 1
            if counter % 1_000_000 == 0:
                print(lines_executed)
            #print('ip: {},  ip_register: {} -> {}'.format(self.ip, self.ip_register, self.registers))
            '''
                Spending lots of time in lines 18-25
                addi 1 1 4
                muli 4 256 4
                gtrr 4 2 4
                addr 4 5 5 <-- registers[5] += registers[4]
                addi 5 1 5 <-- registers[5] += 1
                seti 25 1 5 <-- registers[5] = 25
                addi 1 1 1 <-- registers[1] += 1
                seti 17 0 5 <-- registers[5] = 17
            '''

def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    d = Device(puzzle_input)
    d.run()
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
