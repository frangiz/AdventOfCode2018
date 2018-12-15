"""--- Day 15: Beverage Bandits ---"""
import helpers


class Unit():
    def __init__(self, pos):
        self.pos = pos
        self.attack_power = 3
        self.hp = 200
        self.alive = True

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def attack(self, other):
        other.hp -= self.attack_power


class Elf(Unit):
    def __init__(self, pos):
        super().__init__(pos)

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def get_stats(self):
        return 'E({})'.format(self.hp)


class Goblin(Unit):
    def __init__(self, pos):
        super().__init__(pos)

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def get_stats(self):
        return 'G({})'.format(self.hp)


class FightSimulator():
    def __init__(self, puzzle_input):
        self.elves = []
        self.goblins = []
        self.walls = set()
        self.round = 0
        self.__parse_map(puzzle_input)

    def __parse_map(self, puzzle_input):
        for y in range(len(puzzle_input)):
            for x, c in enumerate(puzzle_input[y]):
                if c == 'E':
                    self.elves.append(Elf(helpers.Point(x, y)))
                elif c == 'G':
                    self.goblins.append(Goblin(helpers.Point(x, y)))
                elif c == '#':
                    self.walls.add(helpers.Point(x, y))

    def tick(self):
        self.round += 1
        turn_order = self.__get_turn_order()
        for unit in turn_order:
            self.__try_move(unit)
            self.__try_attack(unit)

    def __get_turn_order(self):
        sorted_units = []
        max_x = max(self.walls, key=lambda p: p.x).x
        max_y = max(self.walls, key=lambda p: p.y).y
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                unit = self.__get_unit_at_pos(helpers.Point(x, y))
                if unit and unit.alive:
                    sorted_units.append(unit)
        return sorted_units

    def __get_unit_at_pos(self, pos):
        elf = next((e for e in self.elves if e.pos == pos), None)
        goblin = next((g for g in self.goblins if g.pos == pos), None)
        if elf:
            return elf
        elif goblin:
            return goblin
        return None

    def __try_attack(self, unit):
        if type(unit) == Elf:
            adjacent_enemies = self.__get_adjacent_enemies(unit.pos, self.goblins)
        elif type(unit) == Goblin:
            adjacent_enemies = self.__get_adjacent_enemies(unit.pos, self.elves)
        if len(adjacent_enemies) > 0:
            unit.attack(adjacent_enemies[0])

    def __get_adjacent_enemies(self, pos, enemies):
        adjacent_positions = helpers.get_adjecent_4(pos)
        adjacent_enemies = [e for e in enemies if e.pos in adjacent_positions]
        adjacent_enemies.sort(key=lambda u: (u.hp, u.pos.y, u.pos.x))
        return adjacent_enemies

    def __try_move(self, unit):
        if type(unit) == Elf:
            adjacent_enemies = self.__get_adjacent_enemies(unit.pos, self.goblins)
        elif type(unit) == Goblin:
            adjacent_enemies = self.__get_adjacent_enemies(unit.pos, self.elves)
        if len(adjacent_enemies) == 0:
            path = self.__find_shortest_path(unit)
            if path:
                unit.pos = path[1]

    def __find_shortest_path(self, unit):
        paths = self.__find_paths_to_enemies(unit)
        shortest_paths = []
        min_length = 10**5
        for p in paths:
            if len(p) <= min_length:
                shortest_paths.append(p)
                min_length = len(p)
        # TODO: sort the paths
        if len(shortest_paths) == 0:
            return None
        return shortest_paths[0]

    def __find_paths_to_enemies(self, unit):
        if type(unit) == Elf:
            paths = []
            for enemy in self.goblins:
                for path in helpers.shortest_path(unit.pos, enemy.pos, self.__is_open_space):
                    paths.append(path)
            return paths

        if type(unit) == Goblin:
            paths = []
            for enemy in self.elves:
                for path in helpers.shortest_path(unit.pos, enemy.pos, self.__is_open_space):
                    paths.append(path)
            return paths
        return []

    def __is_open_space(self, pos):
        if pos in [elf.pos for elf in self.elves]:
            return False
        if pos in [goblin.pos for goblin in self.goblins]:
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
                p = helpers.Point(x, y)
                elf = next((e for e in self.elves if e.pos == p), None)
                goblin = next((g for g in self.goblins if g.pos == p), None)
                if p in self.walls:
                    print('#', end='')
                elif elf:
                    print('E', end='')
                    stats.append(elf.get_stats())
                elif goblin:
                    print('G', end='')
                    stats.append(goblin.get_stats())
                else:
                    print('.', end='')
            print(' ' * 3, end='')
            print(', '.join(stats))
        print('')


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    sim = FightSimulator(puzzle_input)
    sim.print()
    sim.tick()
    for _ in range(30):
        sim.print()
        sim.tick()
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
