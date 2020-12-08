import unittest
from day8.solution_day8 import parse_instruction


class TestParseInstruction(unittest.TestCase):

    def test_parse_instruction(self):
        instructions = ["acc +3", "jmp -3", "acc -99"]
        actual = [parse_instruction(inst) for inst in instructions]
        expected = [{"acc": 3}, {"jmp": -3}, {"acc": -99}]
        self.assertEqual(actual, expected)
