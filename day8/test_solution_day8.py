import unittest
from day8.solution_day8 import parse_instruction, Program, switch_instruction


class TestParseInstruction(unittest.TestCase):

    def test_parse_instruction(self):
        instructions = ["acc +3", "jmp -3", "acc -99"]
        actual = [parse_instruction(inst) for inst in instructions]
        expected = [("acc", 3), ("jmp", -3), ("acc", -99)]
        self.assertEqual(actual, expected)


class TestJump(unittest.TestCase):

    def test_jump(self):
        pgs = [Program.from_string(pg) for pg in [
            "jmp +2\nnop +0\nnop +0",
            "jmp +1\nnop +0\nnop +0",
            "nop +0\nnop +0\njmp -2",
            "nop +0\nnop +0\njmp -1"
        ]]
        initial_cursor = [0, 0, 2, 2]
        final_cursor = [2, 1, 0, 1]
        for i, pg in enumerate(pgs):
            pg._cursor = initial_cursor[i]
            pg.exe_instruction()
            self.assertEqual(pg._acc, 0)
            self.assertEqual(len(pg._program_execution), 1)
            self.assertEqual(pg._program_execution[-1], initial_cursor[i])
            self.assertEqual(pg._cursor, final_cursor[i])

        error_pgs = [Program.from_string(pg) for pg in [
            "jmp +3\nnop +0\nnop +0",
            "jmp -1\nnop +0\nnop +0"
        ]]
        for pg in error_pgs:
            pg.exe_instruction()
            # now cursor at invalid position, next instruction fails
            self.assertRaises(ValueError, pg.exe_instruction)


class TestNop(unittest.TestCase):

    def test_nop(self):
        pg = Program.from_string("nop +0\nnop -1\nnop +3")
        pg.exe_instruction()
        self.assertEqual(pg._program_execution, [0])
        pg.exe_instruction()
        self.assertEqual(pg._program_execution, [0, 1])
        pg.exe_instruction()
        self.assertEqual(pg._program_execution, [0, 1, 2])
        self.assertEqual(pg._cursor, 3)
        self.assertEqual(pg._acc, 0)


class TestAcc(unittest.TestCase):

    def test_acc(self):
        pg = Program.from_string("acc +0\nacc -1\nacc +3")
        pg.exe_instruction()
        self.assertEqual(pg._acc, 0)
        self.assertEqual(pg._program_execution, [0])
        pg.exe_instruction()
        self.assertEqual(pg._acc, -1)
        self.assertEqual(pg._program_execution, [0, 1])
        pg.exe_instruction()
        self.assertEqual(pg._acc, 2)
        self.assertEqual(pg._program_execution, [0, 1, 2])
        self.assertEqual(pg._cursor, 3)


class TestExecution(unittest.TestCase):

    def test_simple_recurrent_error(self):
        pg = Program.from_string("acc +1\njmp -1")
        self.assertRaises(RecursionError, pg.execute)
        self.assertEqual(pg._cursor, 0)
        self.assertEqual(pg._acc, 1)
        self.assertEqual(pg._program_execution, [0, 1])

    def test_input_recurrent_error(self):
        test_prog = Program.from_file("./day8/test_input.txt")
        self.assertRaises(RecursionError, test_prog.execute)

    def test_input_corrected(self):
        test_prog = Program.from_file("./day8/test_input.txt")
        corrected_prog = switch_instruction(test_prog, 7)
        corrected_prog.execute()
        self.assertEqual(corrected_prog._acc, 8)
