"""The tests for day19."""
from days import day19
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [[
            '#ip 0',
            'seti 5 0 1',
            'seti 6 0 2',
            'addi 0 1 0',
            'addr 1 2 3',
            'setr 1 0 0',
            'seti 8 0 4',
            'seti 9 0 5'], '6'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day19.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day19.part_a(helpers.get_file_contents('day19.txt'))
        self.assertEqual(result, '1728')

    # No example for part b
    '''@data(
        [],
        [])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day19.part_b(test_input)
        self.assertEqual(result, expected)'''

    def test_answer_part_b(self): # noqa D102
        result = day19.part_b(helpers.get_file_contents('day19.txt'))
        self.assertEqual(result, '')
