"""The tests for day02."""
from days import day02
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'], '12'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day02.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day02.part_a(helpers.get_file_contents('day02.txt'))
        self.assertEqual(result, '8892')

    @data(
        [['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz'], 'fgij'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day02.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day02.part_b(helpers.get_file_contents('day02.txt'))
        self.assertEqual(result, 'zihwtxagifpbsnwleydukjmqv')
