import unittest
import numpy as np
from day10.solution_day10 import n_arrangements_aux, unique_counts


class TestUniqueCounts(unittest.TestCase):
    def test_unique_counts(self):
        arrays = [
            np.array([1, 4]),
            np.array([3, 6, 7, 10])
        ]
        expected = [
            np.array([1, 2]),
            np.array([1, 4])
        ]
        for arr, exp in zip(arrays, expected):
            counts = unique_counts(arr)
            self.assertTrue((counts[0] == np.array([1, 3])).all())
            self.assertTrue((counts[1] == exp).all())

class TestArrangements(unittest.TestCase):

    def test_arrangements(self):
        arrays = [
            np.array([3, 3]),
            np.array([3, 3, 3, 3]),
            np.array([3, 3, 3, 1, 3]),
            np.array([3, 3, 1, 1, 3]),
            np.array([3, 1, 1, 1, 3]),
            np.array([3, 1, 1, 1, 1, 3]),
        ]
        expected = [1, 1, 1, 2, 4, 7]
        actual = [n_arrangements_aux(arr, 0, 3, {}) for arr in arrays]
        self.assertEqual(actual, expected)


