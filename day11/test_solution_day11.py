import unittest
import numpy as np
from day11.solution_day11 import (parse_input, read_input,
                                  AdjacentMap, AdjacentSightMap,
                                  update_grid)


class TestInput(unittest.TestCase):

    def test_input_from_list(self):
        test_input = parse_input("#.\nL#".splitlines())
        expected = np.array([["#", "."], ["L", "#"]])
        self.assertTrue((test_input == expected).all())

    def test_input_from_path(self):
        test_input = read_input("./day11/test_input.txt")
        expected00 = "L"
        expected21 = "."
        self.assertEqual(test_input[0, 0], expected00)
        self.assertEqual(test_input[2, 1], expected21)


class TestNAdjacentOccupied(unittest.TestCase):

    def test_get_adjacent(self):
        test_input22 = parse_input("L.\nLL".splitlines())
        adjacent_map = AdjacentMap(test_input22)
        actual = adjacent_map.get_adjacent_coords((0, 0))
        expected = [(1, 0), (1, 1)]
        self.assertEqual(actual, expected)

        test_input33 = parse_input("LL.\n.L.\n..L".splitlines())
        adjacent_map = AdjacentMap(test_input33)
        actual = adjacent_map.get_adjacent_coords((1, 1))
        expected = [(0, 0), (0, 1), (2, 2)]
        self.assertEqual(actual, expected)

    def test_n_adjacent(self):
        initial_grid = parse_input("L.\nLL".splitlines())
        grid = parse_input("#.\nL#".splitlines())
        adjacent_map = AdjacentMap(initial_grid)
        self.assertEqual(adjacent_map.n_adjacent_occupied((0, 0), grid), 1)
        self.assertEqual(adjacent_map.n_adjacent_occupied((1, 0), grid), 2)

    def test_get_adjacent_sight(self):
        test_input55 = \
            parse_input("...LL\n.....\n...LL\nL.L.L\nL.LL.".splitlines())
        adjacent_map = AdjacentSightMap(test_input55)
        actual = adjacent_map.get_adjacent_coords((1, 1))
        self.assertEqual(actual, [])

        actual = adjacent_map.get_adjacent_coords((2, 0))
        expected = [(2, 3), (3, 0), (4, 2)]
        self.assertEqual(actual, expected)


class TestUpdateGrid(unittest.TestCase):

    def test_update_grid(self):
        test_input = read_input("./day11/test_input.txt")
        adjacent_map = AdjacentMap(test_input)
        step1 = update_grid(test_input, adjacent_map, 4)
        self.assertEqual((step1 == "#").sum(), 71)
        step2 = update_grid(step1, adjacent_map, 4)
        self.assertEqual((step2 == "#").sum(), 20)


    def test_update_grid_B(self):
        test_input = read_input("./day11/test_input.txt")
        adjacent_map = AdjacentSightMap(test_input)
        step1 = update_grid(test_input, adjacent_map, 5)
        self.assertEqual((step1 == "#").sum(), 71)
        step2 = update_grid(step1, adjacent_map, 5)
        self.assertEqual((step2 == "#").sum(), 7)
