"""--- Day 24: Immune System Simulator 20XX ---"""
import re
from enum import Enum, auto


class Team(Enum):
    IMMUNESYSTEM = auto()
    INFECTION = auto()


class Group():
    def __init__(self, team, units, hp, weak_to, immune_to, dmg, dmg_type, initiative):
        self.team = team
        self.units = units
        self.hp = hp
        self.weak_to = weak_to
        self.immune_to = immune_to
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.initiative = initiative
        self.target = None
        self.attacked_by = None

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

    def effective_power(self):
        return self.units * self.dmg

    def select_target(self, groups):
        target_stats = (0, 0, 0)
        for g in groups:
            if g.team != self.team and g.attacked_by is None:
                t = (self.calc_damage(g), g.effective_power(), g.initiative)
                if t[0] > 0 and t > target_stats:
                    target_stats = t
                    self.target = g
        if self.target is not None:
            self.target.attacked_by = self

    def calc_damage(self, target):
        if self.dmg_type in target.immune_to:
            return 0
        elif self.dmg_type in target.weak_to:
            return self.effective_power() * 2
        return self.effective_power()

    def attack(self):
        if self.target is not None:
            self.target.units = max(self.target.units - (self.calc_damage(self.target) // self.target.hp), 0)

    def clear_selections(self):
        self.target = None
        self.attacked_by = None


def parse_groups(puzzle_input):
    regex = re.compile(r'(\d+) units each with (\d+) hit points \(([a-z;, ]+)\) with an attack that does (\d+) (\w+) damage at initiative (\d+)') # noqa E501
    regex2 = re.compile(r'(\d+) units each with (\d+) hit points with an attack that does (\d+) (\w+) damage at initiative (\d+)') # noqa E501
    current_team = None
    groups = []
    for line in puzzle_input:
        if line.startswith('Immune System:'):
            current_team = Team.IMMUNESYSTEM
        elif line.startswith('Infection:'):
            current_team = Team.INFECTION
        else:
            s = regex.match(line)
            if s is not None:
                units, hp, weak_and_or_immune_to, dmg, dmg_type, initiative = s.groups()
                weak_to = []
                immune_to = []
                special = sorted(weak_and_or_immune_to.split('; '))
                if special[0].startswith('immune to'):
                    immune_to = special[0].replace('immune to ', '').split(', ')
                elif special[0].startswith('weak to'):
                    weak_to = special[0].replace('weak to ', '').split(', ')
                if len(special) > 1:
                    weak_to = special[1].replace('weak to ', '').split(', ')
                groups.append(Group(current_team, int(units), int(hp), weak_to,
                                    immune_to, int(dmg), dmg_type, int(initiative)))
            s = regex2.match(line)
            if s is not None:
                units, hp, dmg, dmg_type, initiative = s.groups()
                groups.append(Group(current_team, int(units), int(hp), [],
                                    [], int(dmg), dmg_type, int(initiative)))
    return groups


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    groups = parse_groups(puzzle_input)
    while len(set([g.team for g in groups])) > 1:
        groups = sorted(groups, key=lambda g: (g.effective_power(), g.initiative), reverse=True)
        for g in groups:
            g.select_target(groups)
        groups = sorted(groups, key=lambda g: g.initiative, reverse=True)
        for g in groups:
            g.attack()
        [g.clear_selections() for g in groups]
        groups = [g for g in groups if g.units > 0]
    return str(sum(g.units for g in groups))


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_b.

    """
    for boost in range(10**5):
        groups = parse_groups(puzzle_input)
        for g in groups:
            if g.team == Team.IMMUNESYSTEM:
                g.dmg += boost
        while len(set([g.team for g in groups])) > 1:
            units = sum(g.units for g in groups)
            groups = sorted(groups, key=lambda g: (g.effective_power(), g.initiative), reverse=True)
            for g in groups:
                g.select_target(groups)
            groups = sorted(groups, key=lambda g: g.initiative, reverse=True)
            for g in groups:
                g.attack()
            [g.clear_selections() for g in groups]
            groups = [g for g in groups if g.units > 0]
            if units == sum(g.units for g in groups):
                break
        if all(g.team == Team.IMMUNESYSTEM for g in groups):
            return str(sum(g.units for g in groups))
    return str(0)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
