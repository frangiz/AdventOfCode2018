"""--- Day 21: Chronal Conversion ---"""


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
    reg = [0 for _ in range(6)]
    visited = set()
    last_visited = 0
    while True:
        reg[2] = reg[3] | 65536
        reg[3] = 832312
        while True:
            reg[1] = reg[2] & 255
            reg[3] += reg[1]
            reg[3] &= 16777215
            reg[3] *= 65899
            reg[3] &= 16777215
            if 256 > reg[2]:
                if reg[3] == reg[0]:
                    print('This should not happen.')
                    exit()
                else:
                    if reg[3] in visited:
                        return str(last_visited)
                    visited.add(reg[3])
                    last_visited = reg[3]
                    break
            else:
                reg[2] //= 256
    r'''
    #ip 5
    0:  seti 123 0 3        reg[3] = 123
        bani 3 456 3        reg[3] &= 456
        eqri 3 72 3         reg[3] = reg[3] == 72       reg[3] = (123 % 456) == 72
        addr 3 5 5          reg[5] += reg[3]            jmp to #5
        seti 0 0 5          reg[5] = 0
                                                        while True:                                             while True:
    5:  seti 0 5 3          reg[3] = 0                      reg[3] = 0
        bori 3 65536 2      reg[2] = reg[3] | 65536         reg[2] = reg[3] | 65536                                 reg[2] = reg[3] | 65536
        seti 832312 1 3     reg[3] = 832312                 reg[3] = 832312                                         reg[3] = 832312
                                                                                                                    while True:
        bani 2 255 1        reg[1] = reg[2] & 255           reg[1] = reg[2] & 255                                       reg[1] = reg[2] & 255   \
        addr 3 1 3          reg[3] += reg[1]                reg[3] += reg[1]                                            reg[3] += reg[1]        |
    10: bani 3 16777215 3   reg[3] &= 16777215              reg[3] &= 16777215                                          reg[3] &= 16777215      |
        muli 3 65899 3      reg[3] *= 65899                 reg[3] *= 65899                                             reg[3] *= 65899         |
        bani 3 16777215 3   reg[3] &= 16777215              reg[3] &= 16777215                                          reg[3] &= 16777215      /
        gtir 256 2 1        reg[1] = 256 > reg[2]           if 256 > reg[2]:                                            if 256 > reg[2]:
        addr 1 5 5          reg[5] += reg[1]                     go to #28                                                  if reg[3] == reg[0]:
    15: addi 5 1 5          reg[5] += 1                                                                                         exit
        seti 27 7 5         reg[5] = 27                     else:                                                           else:
        seti 0 2 1          reg[1] = 0                          reg[1] = 0          \ while True:                               break
        addi 1 1 4          reg[4] = reg[1] + 1                 reg[4] = reg[1] + 1 |     reg[4] = reg[1] + 1           else:
        muli 4 256 4        reg[4] *= 256                       reg[4] *= 256       |     reg[4] *= 256                     reg[2] //= 256
    20: gtrr 4 2 4          reg[4] = reg[4] > reg[2]            if reg[4] > reg[2]: |     if reg[4] > reg[2]:
        addr 4 5 5          ref[5] += reg[4]                        go to #26       |         break
        addi 5 1 5          reg[5] += 1                         else:               |     reg[1] += 1
        seti 25 1 5         reg[5] = 25                                             |
        addi 1 1 1          reg[1] += 1                             reg[1] += 1     |
    25: seti 17 0 5         reg[5] = 17                             to go #17       /
        setr 1 7 2          reg[2] = reg[1]                 reg[2] = reg[1]
        seti 7 2 5          reg[5] = 7                      go to #7
        eqrr 3 0 1          reg[1] = reg[3] == reg[0]       if reg[3] == reg[0]:
    29: addr 1 5 5          reg[5] += reg[1]                    break
        seti 5 5 5          reg[5] = 5
    '''
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
