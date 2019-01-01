"""The tests for day15."""
from days import day15
from ddt import ddt, data, unpack
import unittest
import helpers


@ddt
class MyTestCase(unittest.TestCase): # noqa D101
    @data(
        [['#######',
          '#.G...#',
          '#...EG#',
          '#.#.#G#',
          '#..G#E#',
          '#.....#',
          '#######'], '27730'],
        [['#######',
          '#G..#E#',
          '#E#E.E#',
          '#G.##.#',
          '#...#E#',
          '#...E.#',
          '#######'], '36334'],
        [['#######',
          '#E..EG#',
          '#.#G.E#',
          '#E.##E#',
          '#G..#.#',
          '#..E#.#',
          '#######'], '39514'],
        [['#######',
          '#E.G#.#',
          '#.#G..#',
          '#G.#.G#',
          '#G..#.#',
          '#...E.#',
          '#######'], '27755'],
        [['#######',
          '#.E...#',
          '#.#..G#',
          '#.###.#',
          '#E#G#G#',
          '#...#G#',
          '#######'], '28944'],
        [['#########',
          '#G......#',
          '#.E.#...#',
          '#..##..G#',
          '#...##..#',
          '#...#...#',
          '#.G...G.#',
          '#.....G.#',
          '#########'], '18740'])
    @unpack
    def test_example_a(self, test_input, expected): # noqa D102
        result = day15.part_a(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_a(self): # noqa D102
        result = day15.part_a(helpers.get_file_contents('day15.txt'))
        self.assertEqual(result, '191575')

    @data(
        [['#######',
          '#.G...#',
          '#...EG#',
          '#.#.#G#',
          '#..G#E#',
          '#.....#',
          '#######'], '4988'],
        [['#######',
          '#E..EG#',
          '#.#G.E#',
          '#E.##E#',
          '#G..#.#',
          '#..E#.#',
          '#######'], '31284'],
        [['#######',
          '#E.G#.#',
          '#.#G..#',
          '#G.#.G#',
          '#G..#.#',
          '#...E.#',
          '#######'], '3478'],
        [['#######',
          '#.E...#',
          '#.#..G#',
          '#.###.#',
          '#E#G#G#',
          '#...#G#',
          '#######'], '6474'],
        [['#########',
          '#G......#',
          '#.E.#...#',
          '#..##..G#',
          '#...##..#',
          '#...#...#',
          '#.G...G.#',
          '#.....G.#',
          '#########'], '1140'])
    @unpack
    def test_example_b(self, test_input, expected): # noqa D102
        result = day15.part_b(test_input)
        self.assertEqual(result, expected)

    def test_answer_part_b(self): # noqa D102
        result = day15.part_b(helpers.get_file_contents('day15.txt'))
        self.assertEqual(result, '75915')
