import unittest
from day9.solution_day9 import (read_input, is_sum_of_two,
                                find_contiguous_sum_equal_to)


class TestIsSumOfTwo(unittest.TestCase):

    def test_sum_of_two(self):
        array = read_input("./day9/test_input.txt")
        is_valid = [is_sum_of_two(i, 5, array) for i in range(5, len(array))]
        self.assertFalse(is_valid[9])
        del is_valid[9]
        self.assertTrue(all(is_valid))


class TestContiguous(unittest.TestCase):

    def test_contiguous(self):
        array = read_input("./day9/test_input.txt")
        sub = find_contiguous_sum_equal_to(127, array)
        self.assertEqual(sum(sub), 127)
        self.assertTrue((sub == [15, 25, 47, 40]).all())
