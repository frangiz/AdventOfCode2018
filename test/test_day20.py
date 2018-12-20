"""The tests for day20."""
from days import day20
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['^WNE$'], '3'],
        [['^ENWWW(NEEE|SSE(EE|N))$'], '10'],
        [['^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'], '18'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day20.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day20.part_a(helpers.get_file_contents('day20.txt'))
        self.assertEqual(result, '4344')

    # No examples for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day20.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day20.part_b(helpers.get_file_contents('day20.txt'))
        self.assertEqual(result, '8809')
