import unittest
from day5.solution_day5 import decode_seat_id

class TestDecodeSeatId(unittest.TestCase):

    def test_decode_seat_id(self):
        seats = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        expected_ids = [567, 119, 820]
        actual_ids = [decode_seat_id(s) for s in seats]
        self.assertTrue(expected_ids == actual_ids)
