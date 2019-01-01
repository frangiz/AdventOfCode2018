"""--- Day 15: Beverage Bandits ---"""
from helpers import Point, get_adjecent_4
import enum
from collections import deque


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


class Unit():
    def __init__(self, pos, team, attack_power=3):
        self.pos = pos
        self.attack_power = attack_power
        self.hp = 200
        self.alive = True
        self.team = team

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def attack(self, other):
        other.hp -= self.attack_power
        if other.hp <= 0:
            other.alive = False

    def get_stats(self):
        return '{}({})'.format(self.team, self.hp)


class FightSimulator():
    def __init__(self, puzzle_input, elf_attack_power=3):
        self.units = []
        self.walls = set()
        self.round = 0
        self.__parse_map(puzzle_input, elf_attack_power)

    def __parse_map(self, puzzle_input, elf_attack_power):
        for y in range(len(puzzle_input)):
            for x, c in enumerate(puzzle_input[y]):
                if c == 'E':
                    self.units.append(Unit(Point(x, y), Team.ELF, attack_power=elf_attack_power))
                elif c == 'G':
                    self.units.append(Unit(Point(x, y), Team.GOBLIN))
                elif c == '#':
                    self.walls.add(Point(x, y))

    def tick(self):
        complete_round = True
        for unit in sorted(self.units, key=lambda u: (u.pos.y, u.pos.x)):
            if unit.alive:
                if self.__has_enemies(unit):
                    self.__try_move(unit)
                    self.__try_attack(unit)
                else:
                    complete_round = False
                    break
        self.units = [u for u in self.units if u.alive]
        if complete_round:
            self.round += 1

    def __has_enemies(self, unit):
        return any(u for u in self.units if u.team != unit.team and u.alive)

    def __try_attack(self, unit):
        adjacent_enemies = self.__get_adjacent_enemies(unit)
        if len(adjacent_enemies) > 0:
            unit.attack(adjacent_enemies[0])

    def __get_adjacent_enemies(self, unit):
        adjacent_enemies = []
        for pos in get_adjecent_4(unit.pos):
            enemy = next((e for e in self.units if e.team != unit.team and e.alive and e.pos == pos), None)
            if enemy:
                adjacent_enemies.append(enemy)
        adjacent_enemies.sort(key=lambda u: (u.hp, u.pos.y, u.pos.x))
        return adjacent_enemies

    def __try_move(self, unit):
        adjacent_enemies = self.__get_adjacent_enemies(unit)
        if len(adjacent_enemies) == 0:
            path = self.__find_closest_enemy(unit)
            if path:
                unit.pos = path[1]

    def __find_closest_enemy(self, unit):
        frontier = deque()
        start = Point(unit.pos.x, unit.pos.y)
        frontier.append(start)
        came_from = {}
        came_from[start] = None
        team_mates = set([u.pos for u in self.units if u.team == unit.team and u.alive])
        while frontier:
            current = frontier.popleft()
            for new_position in sorted(get_adjecent_4(current), key=lambda p: (p.y, p.x)):
                if new_position not in self.walls and new_position not in came_from and new_position not in team_mates:
                    frontier.append(new_position)
                    came_from[new_position] = current
        targets = []
        for u in self.units:
            if u.team != unit.team and u.alive:
                targets.extend(get_adjecent_4(u.pos))
        paths = []
        for current in sorted(targets, key=lambda p: (p.y, p.x)):
            if current in came_from:
                path = []
                while current != start:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                paths.append(path)
        if len(paths) == 0:
            return None
        return min(paths, key=len)

    def __is_open_space(self, pos):
        if pos in [unit.pos for unit in self.units if unit.alive]:
            return False
        if pos in self.walls:
            return False
        return True

    def print(self):
        max_x = max(self.walls, key=lambda p: p.x).x
        max_y = max(self.walls, key=lambda p: p.y).y
        print('Round: {}'.format(self.round))
        for y in range(max_y + 1):
            stats = []
            for x in range(max_x + 1):
                p = Point(x, y)
                unit = next((u for u in self.units if u.pos == p and u.alive), None)
                if p in self.walls:
                    print('#', end='')
                elif unit:
                    print('{}'.format('E' if unit.team == Team.ELF else 'G'), end='')
                    stats.append(unit.get_stats())
                else:
                    print('.', end='')
            print(' ' * 3, end='')
            print(', '.join(stats))
        print('')

    def calc_outcome(self):
        while True:
            self.tick()
            if len([e for e in self.units if e.team == Team.ELF and e.alive]) == 0:
                return sum(g.hp for g in self.units if g.alive and g.team == Team.GOBLIN) * self.round
            if len([g for g in self.units if g.team == Team.GOBLIN and g.alive]) == 0:
                return sum(e.hp for e in self.units if e.alive and e.team == Team.ELF) * self.round
        return 0


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    sim = FightSimulator(puzzle_input)
    return str(sim.calc_outcome())


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    sim = FightSimulator(puzzle_input)
    nbr_of_elves = len([e for e in sim.units if e.team == Team.ELF and e.alive])
    for i in range(4, 5**10):
        sim = FightSimulator(puzzle_input, elf_attack_power=i)
        while True:
            sim.tick()
            elves_alive = len([e for e in sim.units if e.team == Team.ELF and e.alive])
            goblins_alive = len([g for g in sim.units if g.team == Team.GOBLIN and g.alive])
            if elves_alive != nbr_of_elves:
                break
            if goblins_alive == 0:
                return str(sum(e.hp for e in sim.units if e.alive and e.team == Team.ELF) * sim.round)
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
