import unittest
from solution_day3 import *

def get_test_input_small():
    return parse_forest([".#.","..#", "###"])

def get_test_input():
    return read_forest("./test_input.txt")

class TestParseForest(unittest.TestCase):

    def test_input(self):
        input_arr = get_test_input_small()
        expected_arr = np.array([[0, 1, 0], [0, 0 , 1], [1, 1, 1]])
        self.assertTrue(type(input_arr) is np.ndarray)
        self.assertTrue((input_arr == expected_arr).all())

class TestReadForest(unittest.TestCase):

    def test_input(self):
        input_arr = get_test_input()
        self.assertEqual(input_arr.shape, (11, 11))

class TestIsATree(unittest.TestCase):

    def test_is_a_tree(self):
        input_arr = get_test_input_small()
        self.assertEqual(is_a_tree(input_arr, [(0, 0)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, 1)]), [True])
        self.assertTrue(
            all(is_a_tree(input_arr, [(2, 0), (2, 1)]))
        )

    def test_recycle_forest_left(self):
        input_arr = get_test_input_small()
        self.assertEqual(is_a_tree(input_arr, [(0, -1)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, -2)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, -4)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, -5)]), [False])
        self.assertTrue(all(is_a_tree(input_arr, [(0, -2), (1, -4)])))

    def test_recycle_forest_left(self):
        input_arr = get_test_input_small()
        self.assertEqual(is_a_tree(input_arr, [(0, 5)]), [False])
        self.assertEqual(is_a_tree(input_arr, [(0, 4)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, 8)]), [True])
        self.assertEqual(is_a_tree(input_arr, [(1, 7)]), [False])
        self.assertTrue(all(is_a_tree(input_arr, [(0, 4), (1, 8)])))

    def test_value(self):
        input_arr = get_test_input_small()
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(-1, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(3, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(0, 1), (3, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, [(-1, -1), (0, 0)])
        with self.assertRaises(ValueError):
            is_a_tree(input_arr, (-1, -1))

class TestTreeCount(unittest.TestCase):

    def test_count_trees(self):
        forest = get_test_input_small()
        self.assertEqual(count_trees_on_way((1, 1), forest), 1)
        self.assertEqual(count_trees_on_way((1, -1), forest), 2)
        self.assertEqual(count_trees_on_way((1, 2), forest), 2)
        forest2 = get_test_input()
        self.assertEqual(count_trees_on_way((1, 3), forest2), 7)

if __name__ == "__main__":
    unittest.main()
