"""--- Day 15: Beverage Bandits ---"""
from helpers import Point, get_adjecent_4
import enum
from collections import deque


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


class Unit():
    def __init__(self, pos, team):
        self.pos = pos
        self.attack_power = 3
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
    def __init__(self, puzzle_input):
        self.units = []
        self.walls = set()
        self.round = 0
        self.__parse_map(puzzle_input)

    def __parse_map(self, puzzle_input):
        for y in range(len(puzzle_input)):
            for x, c in enumerate(puzzle_input[y]):
                if c == 'E':
                    self.units.append(Unit(Point(x, y), Team.ELF))
                elif c == 'G':
                    self.units.append(Unit(Point(x, y), Team.GOBLIN))
                elif c == '#':
                    self.walls.add(Point(x, y))

    def tick(self):
        complete_round = True
        for unit in sorted(self.units, key=lambda u: (u.pos.y, u.pos.x)):
            if unit.alive:
                print('Activating unit: {}'.format(unit))
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
            enemy = next((e for e in self.units if
                          e.team != unit.team and e.alive and 
                          e.pos.x == pos.x and e.pos.y == pos.y), None)
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
        class Node:
            def __init__(self, pos, length, parent):
                self.pos = pos
                self.length = length
                self.parent = parent
        unvisited = deque()
        solution = None
        targets = [u.pos for u in self.units if u.team != unit.team and u.alive]
        unvisited.append(Node(unit.pos, 0, None))
        visited = set()
        team_mates = set([u.pos for u in self.units if u.team == unit.team and u.alive])
        while unvisited:
            node = unvisited.popleft()
            if node.pos in targets:
                solution = node
                break
            visited.add(node.pos)
            for new_position in sorted(get_adjecent_4(node.pos), key=lambda p: (p.y, p.x)):
                if new_position not in self.walls and new_position not in visited and new_position not in team_mates:
                    unvisited.append(Node(new_position, node.length + 1, node))
        if solution is None:
            return None
        path = []
        while node.parent is not None:
            path.append(node.pos)
            node = node.parent
        path.append(node.pos)
        path.reverse()
        return path

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
            elves_alive = len([e for e in self.units if e.team == Team.ELF and e.alive])
            goblins_alive = len([g for g in self.units if g.team == Team.GOBLIN and g.alive])
            print('elves: {}, goblins: {}'.format(elves_alive, goblins_alive))
            if len([e for e in self.units if e.team == Team.ELF and e.alive]) == 0:
                print('rounds: {}'.format(self.round))
                print(self.print())
                return sum(g.hp for g in self.units if g.alive and g.team == Team.GOBLIN) * self.round
            if len([g for g in self.units if g.team == Team.GOBLIN and g.alive]) == 0:
                print('rounds: {}'.format(self.round))
                print(self.print())
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
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
