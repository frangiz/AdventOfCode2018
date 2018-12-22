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
            if self.registers[4] > self.registers[2]:
                print(self.registers)
                #print(lines_executed)
                
            #print('ip: {},  ip_register: {} -> {}'.format(self.ip, self.ip_register, self.registers))
            '''
                #ip 5
                seti 123 0 3     <-- registers[3] = 123
                bani 3 456 3     <-- registers[3] = registers[3] & 456
                eqri 3 72 3      <-- registers[3] = registerse[3] == 72
                addr 3 5 5       <-- registers[5] += registers[3]
                seti 0 0 5       <-- registers[5] = 0
                5:  seti 0 5 3   <-- registers[3] = 0
                bori 3 65536 2   <-- registers[2] = registers[3] | 65536
                seti 832312 1 3  <-- registers[3] = 832312
                bani 2 255 1     <-- registers[1] = registers[2] & 0xFF
                addr 3 1 3       <-- registers[3] += registers[1]
                10: bani 3 16777215 3 <-- registers[3] = registers[3] & 0xFFFFFF
                muli 3 65899 3      <-- registers[3] = registers[3] * 65899
                bani 3 16777215 3   <-- registers[3] = registers[3] & 0xFFFFFF
                gtir 256 2 1        <-- registers[1] = 256 > registers[2]
                addr 1 5 5          <-- registers[5] += registers[1]
                15: addi 5 1 5      <-- registers[5] += 1
                seti 27 7 5         <-- registers[5] = 27
                17: seti 0 2 1      <-- registers[1] = 0

                Spending lots of time in lines 18-25
                addi 1 1 4      <-- registers[4] = registers[1] + 1
                muli 4 256 4    <-- registers[4] *= 256
                gtrr 4 2 4      <-- registers[4] = registers[4] > registers[2]
                addr 4 5 5      <-- registers[5] += registers[4]
                22: addi 5 1 5  <-- registers[5] += 1
                seti 25 1 5     <-- registers[5] = 25 # <-- break the loop?
                addi 1 1 1      <-- registers[1] += 1
                25: seti 17 0 5 <-- registers[5] = 17 # jump back to 18

                setr 1 7 2      <-- registers[2] = registers[1]
                seti 7 2 5      <-- registers[5] = 7
                eqrr 3 0 1      <-- registers[1] = registers[3] == registers[0]
                addr 1 5 5      <-- registers[5] += registers[1]
                seti 5 5 5      <-- registers[5] = 5
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
    print(d.registers)
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
