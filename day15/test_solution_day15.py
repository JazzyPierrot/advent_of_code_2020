import unittest
from day15.solution_day15 import number_at_step


def initial_test():
    return {0: 1, 3: 2, 6: 3}

class TestNext(unittest.TestCase):

    def test_next(self):
        self.assertEqual(number_at_step(initial_test(), 4), 0)
        self.assertEqual(number_at_step(initial_test(), 5), 3)
        self.assertEqual(number_at_step(initial_test(), 6), 3)
        self.assertEqual(number_at_step(initial_test(), 7), 1)


class TestCases(unittest.TestCase):

    def test_2020_number(self):
        initial_dicts = [
            {1: 1, 3: 2, 2: 3},
            {2: 1, 1: 2, 3: 3},
            {1: 1, 2: 2, 3: 3},
            {2: 1, 3: 2, 1: 3},
            {3: 1, 2: 2, 1: 3},
            {3: 1, 1: 2, 2: 3}
        ]
        actual = [number_at_step(d, 2020) for d in initial_dicts]
        expected = [1, 10, 27, 78, 438, 1836]
        self.assertEqual(actual, expected)


    def test_30M_number(self):
        initial_dicts = [
            {1: 1, 3: 2, 2: 3},
            {2: 1, 1: 2, 3: 3},
            {1: 1, 2: 2, 3: 3},
            {2: 1, 3: 2, 1: 3},
            {3: 1, 2: 2, 1: 3},
            {3: 1, 1: 2, 2: 3}
        ]
        # actual = [number_n(d, 30000000) for d in initial_dicts]
        # expected = [2578, 3544142, 261214, 6895259, 18, 362]
        # self.assertEqual(actual, expected)
