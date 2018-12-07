"""The tests for day07."""
from days import day07
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['Step C must be finished before step A can begin.',
            'Step C must be finished before step F can begin.',
            'Step A must be finished before step B can begin.',
            'Step A must be finished before step D can begin.',
            'Step B must be finished before step E can begin.',
            'Step D must be finished before step E can begin.',
            'Step F must be finished before step E can begin.'], 'CABDFE'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day07.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day07.part_a(helpers.get_file_contents('day07.txt'))
        self.assertEqual(result, 'BETUFNVADWGPLRJOHMXKZQCISY')

    @data(
        [['Step C must be finished before step A can begin.',
            'Step C must be finished before step F can begin.',
            'Step A must be finished before step B can begin.',
            'Step A must be finished before step D can begin.',
            'Step B must be finished before step E can begin.',
            'Step D must be finished before step E can begin.',
            'Step F must be finished before step E can begin.'], '15'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day07.part_b(test_input, workers=2, offset=0)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day07.part_b(helpers.get_file_contents('day07.txt'))
        self.assertEqual(result, '848')
