"""The tests for day09."""
from days import day09
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['9 players; last marble is worth 25 points'], '32'],
        [['10 players; last marble is worth 1618 points'], '8317'],
        [['13 players; last marble is worth 7999 points'], '146373'],
        [['17 players; last marble is worth 1104 points'], '2764'],
        [['21 players; last marble is worth 6111 points'], '54718'],
        [['30 players; last marble is worth 5807 points'], '37305'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day09.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day09.part_a(helpers.get_file_contents('day09.txt'))
        self.assertEqual(result, '398048')

    # No examples for part b
    '''@data(
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day09.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day09.part_b(helpers.get_file_contents('day09.txt'))
        self.assertEqual(result, '3180373421')
