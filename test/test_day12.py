"""The tests for day12."""
from days import day12
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            'initial state: #..#.#..##......###...###',
            '',
            '...## => #',
            '..#.. => #',
            '.#... => #',
            '.#.#. => #',
            '.#.## => #',
            '.##.. => #',
            '.#### => #',
            '#.#.# => #',
            '#.### => #',
            '##.#. => #',
            '##.## => #',
            '###.. => #',
            '###.# => #',
            '####. => #'], '325'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day12.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day12.part_a(helpers.get_file_contents('day12.txt'))
        self.assertEqual(result, '2040')

    # No example for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day12.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day12.part_b(helpers.get_file_contents('day12.txt'))
        self.assertEqual(result, '1700000000011')
