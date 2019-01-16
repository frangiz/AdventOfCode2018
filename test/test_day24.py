"""The tests for day24."""
from days import day24
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            'Immune System:',
            '17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2',  # noqa E501
            '989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3',  # noqa E501
            '',
            'Infection:',
            '801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1',  # noqa E501
            '4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'],  # noqa E501
            '5216'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day24.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day24.part_a(helpers.get_file_contents('day24.txt'))
        self.assertEqual(result, '17738')

    @data(
        [[
            'Immune System:',
            '17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2',  # noqa E501
            '989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3',  # noqa E501
            '',
            'Infection:',
            '801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1',  # noqa E501
            '4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4'],  # noqa E501
            '51'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day24.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day24.part_b(helpers.get_file_contents('day24.txt'))
        self.assertEqual(result, '3057')
