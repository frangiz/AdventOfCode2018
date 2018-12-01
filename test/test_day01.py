"""The tests for day01."""
from days import day01
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['+1', '+1', '+1'], '3'],
        [['+1', '+1', '-2'], '0'],
        [['-1', '-2', '-3'], '-6'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day01.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day01.part_a(helpers.get_file_contents('day01.txt'))
        self.assertEqual(result, '406')

    @data(
        [['+1', '-1'], '0'],
        [['+3', '+3', '+4', '-2', '-4'], '10'],
        [['-6', '+3', '+8', '+5', '-6'], '5'],
        [['+7', '+7', '-2', '-7', '-4'], '14'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day01.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day01.part_b(helpers.get_file_contents('day01.txt'))
        self.assertEqual(result, '312')
