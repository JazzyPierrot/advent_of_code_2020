import unittest
from numpy import nan
import pandas as pd
from common.aoc_functions import split_batch
from day4.solution_day4 import (parse_pass, read_pass_batch,
                                are_valid_passes_A, are_valid_passes_B)

class TestSplitPassBatch(unittest.TestCase):

    def test_split_pass_batch(self):
        test_pass_batch = (
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd" "\n"
            "byr:1937 iyr:2017 cid:147 hgt:183cm" "\n"
            "\n"
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884" "\n"
            "hcl:#cfa07d byr:1929" "\n"
        )
        expected = [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
        ]
        actual = [l for l in split_batch(test_pass_batch.splitlines(), ' ')]
        self.assertEqual(actual, expected)

class TestParsePass(unittest.TestCase):

    def test_parse_pass(self):
        test_pass1 = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
        expected1 = {
            "ecl":"gry",
            "pid":"860033327",
            "eyr":"2020",
            "hcl":"#fffffd",
            "byr":"1937",
            "iyr":"2017",
            "cid":"147",
            "hgt":"183cm"
        }
        test_pass2 = "iyr:2013 ecl:amb"
        expected2 = {"iyr":"2013", "ecl":"amb"}
        self.assertEqual(parse_pass(test_pass1), expected1)
        self.assertEqual(parse_pass(test_pass2), expected2)

class TestReadBatch(unittest.TestCase):

    def test_read_batch(self):
        actual = read_pass_batch("./day4/test_input.txt")
        self.assertEqual(actual.shape[0], 251)

class TestValidPass(unittest.TestCase):

    def test_valid_pass(self):
        valid_passes_A = pd.DataFrame([
            ["1937", "2017", "2020", "18", "#ff", "g", "8", "1"],
            ["1937", "2017", "2020", "18", "#ff", "g", "8", nan]
        ],
                                      columns = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",
                                                 "cid"))

        invalid_passes_A = pd.DataFrame([
            [nan, "2017", "2020", "18", "#ff", "g", "8", "1"],
            ["1937", nan, "2020", "18", "#ff", "g", "8", "1"],
            ["1937", "2017", nan, "18", "#ff", "g", "8", "1"],
            ["1937", "2017", "2020", nan, "#ff", "g", "8", "1"],
            ["1937", "2017", "2020", "18", nan, "g", "8", "1"],
            ["1937", "2017", "2020", "18", "#ff", nan, "8", "1"],
            ["1937", "2017", "2020", "18", "#ff", "g", nan, "1"]
        ], columns = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",
                      "cid"))
        self.assertTrue(are_valid_passes_A(valid_passes_A).all())
        self.assertFalse(are_valid_passes_A(invalid_passes_A).any())

        valid_passes_B = read_pass_batch("./day4/sample_valid_B.txt")
        invalid_passes_B = read_pass_batch("./day4/sample_invalid_B.txt")

        self.assertTrue(are_valid_passes_B(valid_passes_B).all())
        self.assertFalse(are_valid_passes_B(invalid_passes_B).any())


if __name__ == "__main__":
    unittest.main()

