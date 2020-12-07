import unittest
from day1.day1_solution import find_combination_given_sum

class TestPairGivenSum(unittest.TestCase):

    def test_values(self):
        self.assertEqual(
           find_combination_given_sum([1721, 979, 366, 299, 675, 1456], 2, 2020),
           (1721, 299)
        )
        self.assertIsNone(find_combination_given_sum([1010], 2, 2020))
        self.assertIsNone(find_combination_given_sum([0, 0, 0], 2, 2020))

    def test_emptylist(self):
        self.assertIsNone(find_combination_given_sum([], 2, 2020))


class TestTrioGivenSum(unittest.TestCase):

    def test_values(self):
        self.assertEqual(
           find_combination_given_sum([1721, 979, 366, 299, 675, 1456], 3, 2020),
           (979, 366, 675)
        )
        self.assertIsNone(find_combination_given_sum([1000, 20], 3, 2020))
        self.assertIsNone(find_combination_given_sum([0, 0, 0], 3, 2020))

    def test_shortlist(self):
        self.assertIsNone(find_combination_given_sum([], 3, 2020))
        self.assertIsNone(find_combination_given_sum([2020], 3, 2020))

if __name__ == '__main__':
    unittest.main()
