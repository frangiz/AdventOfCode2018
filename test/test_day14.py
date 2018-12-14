"""The tests for day14."""
from days import day14
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['9'], '5158916779'],
        [['5'], '0124515891'],
        [['18'], '9251071085'],
        [['2018'], '5941429882'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day14.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day14.part_a(helpers.get_file_contents('day14.txt'))
        self.assertEqual(result, '2107929416')

    @data(
        [['51589'], '9'],
        [['01245'], '5'],
        [['92510'], '18'],
        [['59414'], '2018'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day14.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day14.part_b(helpers.get_file_contents('day14.txt'))
        self.assertEqual(result, '20307394')
