import unittest
from day14.solution_day14 import (MemoryWriter, MemoryWriterB)


class TestMaskParsing(unittest.TestCase):

    def test_parse_mask(self):
        mw = MemoryWriter()
        mask = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        actual = mw.parse_mask(mask)
        expected = (
            int('000000000000000000000000000001000000', 2),
            int('111111111111111111111111111111111101', 2)
        )
        self.assertEqual(actual, expected)


class TestMemParsing(unittest.TestCase):

    def test_parse_mem(self):
        mw = MemoryWriter()
        mem = "mem[123] = 4567"
        actual = mw.parse_memory_instruction(mem)
        expected = (123, 4567)
        self.assertEqual(actual, expected)


class TestMemoryWriter(unittest.TestCase):

    def test_write_memory(self):
        mw = MemoryWriter()
        mw.write_to_memory(3, 4)
        self.assertEqual(mw.memory, {4: 3})
        mw.write_to_memory(5, 4)
        self.assertEqual(mw.memory, {4: 5})
        mw.write_to_memory(1, 2)
        self.assertEqual(mw.memory, {2: 1, 4: 5})

    def test_value_error(self):
        mw = MemoryWriter()
        self.assertRaises(ValueError, mw.write_to_memory, -1, 2)
        self.assertRaises(ValueError, mw.write_to_memory, 2 ** 33, 2)

    def test_mask(self):
        mw = MemoryWriter()
        mw.or_mask, mw.and_mask = mw.parse_mask(
            "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        )
        mw.write_to_memory(11, 8)
        mw.write_to_memory(101, 7)
        mw.write_to_memory(0, 8)
        self.assertEqual(mw.memory, {8: 64, 7: 101})

    def test_instructions(self):
        with open("./day14/test_input.txt") as f:
            mw = MemoryWriter(f)
            mw.read_instructions()
        self.assertEqual(sum(mw.memory.values()), 165)


class TestMemoryWriterB(unittest.TestCase):

    def test_float_addresses(self):
        mw = MemoryWriterB()
        mw.or_mask = "00000000000000000000000000000000000X"
        fa = list(mw.generate_float_addresses(4))
        self.assertEqual(fa, [4, 5])
        mw.or_mask = "00000000000000000000000000000000X0XX"
        fa = list(mw.generate_float_addresses(16))
        self.assertEqual(fa, [16, 17, 18, 19, 24, 25, 26, 27])

    def test_instructions(self):
        with open("./day14/test_inputB.txt") as f:
            mw = MemoryWriterB(f)
            mw.read_instructions()
        print()
        print(mw.memory)
        self.assertEqual(sum(mw.memory.values()), 208)
