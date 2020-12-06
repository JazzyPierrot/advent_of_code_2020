import unittest
from solution_day5 import read_unique_answers


class TestUniqueAnswers(unittest.TestCase):

    def test_unique_answers(self):
        actual_answers = read_unique_answers("./test_input.csv")
        expected = [
            set({"a", "b", "c"}),
            set({"a", "b", "c"}),
            set({"a", "b", "c"}),
            set({"a"}),
            set({"b"})
        ]
        self.assertTrue(all(actual_answers == expected))



if __name__ == "__main__":
    unittest.main()

