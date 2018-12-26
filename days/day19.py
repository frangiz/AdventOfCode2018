"""--- Day 19: Go With The Flow ---"""


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

    def run(self, optimize=False):
        while 0 <= self.ip < len(self.instructions):
            op, a, b, c = self.instructions[self.ip].split()
            if optimize and self.ip == 1:
                self.registers[3] = 1
                while self.registers[3] <= self.registers[4]:
                    if self.registers[4] % self.registers[3] == 0:
                        self.registers[0] += self.registers[3]
                    self.registers[3] += 1
                self.registers[1] = self.registers[4] + 1
                self.registers[2] = 16
                self.registers[5] = 1
                self.ip = 16
                continue
            self.registers[self.ip_register] = self.ip
            self.cmds[op](int(a), int(b), int(c))
            self.ip = self.registers[self.ip_register] + 1


def part_a(puzzle_input, optimize=False):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    d = Device(puzzle_input)
    d.run(optimize=optimize)
    return str(d.registers[0])


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    d = Device(puzzle_input)
    d.registers[0] = 1
    d.run(optimize=True)

    r'''
    Two loops have been identified:
        * an inner loop with instruction #2-11
        * an outer loop with instruction #1-15
    #ip 2
    0 : addi 2 16 2     reg[2] += 16
        seti 1 4 3      reg[3] = 1
                                                    \ while True:                         \
        seti 1 5 1      reg[1] = 1                  |     reg[1] = 1                      | if reg[4] % reg[3] == 0:
        mulr 3 1 5      reg[5] = reg[3] * reg[1]    |                                     |     reg[0] += reg[3]
        eqrr 5 4 5      reg[5] = reg[5] == reg[4]   |     if (reg[3] * reg[1]) == reg[4]: | reg[1] = reg[4] + 1
    5:  addr 5 2 2      reg[2] += reg[5]      jmp?  |                                     | reg[2] = 12
        addi 2 1 2      reg[2] += 1                 |                                     | reg[5] = 1
        addr 3 0 0      reg[0] += reg[3]            |         reg[0] += reg[3]            | self.ip = 12
        addi 1 1 1      reg[1] += 1                 |     reg[1] += 1                     |
        gtrr 1 4 5      reg[5] = reg[1] > reg[4]    |     if reg[1] > reg[4]:             |
    10: addr 2 5 2      reg[2] += reg[5]            |         break -> go to #12          |
        seti 2 9 2      reg[2] = 2                  / jmp back to #2                      /
    12: addi 3 1 3      reg[3] += 1                             \   reg[3] += 1
        gtrr 3 4 5      reg[5] = reg[3] > reg[4]                |   if reg[3] > reg[4]:
        addr 5 2 2      reg[2] += reg[5]                        |       break loop and go to #16
                                                                |   else:
    15: seti 1 6 2      reg[2] = 1                              /       else go to #1
        mulr 2 2 2      reg[2] *= reg[2] <-- squaring the value
    17: addi 4 2 4      reg[4] += 2
        mulr 4 4 4      reg[4] *= reg[4] <-- squaring the value
        mulr 2 4 4      reg[4] *= reg[2]
    20: muli 4 11 4     reg[4] *= 11
        addi 5 7 5      reg[5] += 7
        mulr 5 2 5      reg[5] *= reg[2]
        addi 5 4 5      reg[5] += 4
        addr 4 5 4      reg[4] += reg[5]
    25: addr 2 0 2      reg[2] += reg[0]
        seti 0 1 2      reg[2] = 0
        setr 2 1 5      reg[5] = reg[2]
        mulr 5 2 5      reg[5] *= reg[2]
        addr 2 5 5      reg[5] += reg[2]
    30: mulr 2 5 5      reg[5] *= reg[2]
        muli 5 14 5     reg[5] *= 14
        mulr 5 2 5      reg[5] *= reg[2]
        addr 4 5 4      reg[4] += reg[5]
        seti 0 6 0      reg[0] = 0
    35: seti 0 6 2      reg[2] = 0
    '''
    return str(d.registers[0])


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
