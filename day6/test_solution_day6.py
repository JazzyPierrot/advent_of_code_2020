import unittest
from day6.solution_day6 import read_unique_answers, read_common_answers


class TestUniqueAnswers(unittest.TestCase):

    def test_unique_answers(self):
        actual_answers = read_unique_answers("./day6/test_input.txt")
        expected = [
            set({"a", "b", "c"}),
            set({"a", "b", "c"}),
            set({"a", "b", "c"}),
            set({"a"}),
            set({"b"})
        ]
        self.assertTrue(actual_answers == expected)

class TestCommonAnswers(unittest.TestCase):

    def test_common_answers(self):
        actual_answers = read_common_answers("./day6/test_input.txt")
        expected = [
            set({"a", "b", "c"}),
            set({}),
            set({"a"}),
            set({"a"}),
            set({"b"})
        ]
        self.assertTrue(actual_answers == expected)

if __name__ == "__main__":
    unittest.main()

