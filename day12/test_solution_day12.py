import unittest
from day12.solution_day12 import (parse_action, Ship, read_actions,
                                  ShipWaypoint)


class TestParseAction(unittest.TestCase):

    def test_parse_action(self):
        actions = ["F10", "N3", "F7", "R90", "F11"]
        expected = [
            ("F", 10),
            ("N", 3),
            ("F", 7),
            ("R", 90),
            ("F", 11)
        ]
        self.assertEqual([parse_action(a) for a in actions], expected)


class TestShipActions(unittest.TestCase):

    def assert_posdir(self, ship, position, direction):
        self.assertEqual(ship.position, position)
        self.assertEqual(ship.direction, direction)

    def test_forward(self):
        ship = Ship()
        ship.take_action(("F", 3))
        self.assert_posdir(ship, [3, 0], [1, 0])
        ship.direction = [-1, 1]
        ship.take_action(("F", 2))
        self.assert_posdir(ship, [1, 2], [-1, 1])

    def test_cardinal_points(self):
        ship = Ship()
        ship.take_action(("N", 10))
        self.assert_posdir(ship, [0, 10], [1, 0])
        ship.take_action(("S", 10))
        self.assert_posdir(ship, [0, 0], [1, 0])

        ship = Ship()
        ship.take_action(("E", 10))
        self.assert_posdir(ship, [10, 0], [1, 0])
        ship.take_action(("W", 10))
        self.assert_posdir(ship, [0, 0], [1, 0])

    def test_turn(self):
        ship = Ship()
        ship.take_action(("L", 90))
        self.assert_posdir(ship, [0, 0], [0, 1])
        ship.take_action(("L", 90))
        self.assert_posdir(ship, [0, 0], [-1, 0])

        ship = Ship()
        ship.take_action(("R", 90))
        self.assert_posdir(ship, [0, 0], [0, -1])


class testManhDistance(unittest.TestCase):

    def test_input(self):
        ship = Ship()
        actions = read_actions("./day12/test_input.txt")
        for a in actions:
            ship.take_action(a)
        self.assertEqual(abs(ship.position[0]) + abs(ship.position[1]), 25)

    def test_waypoint(self):
        ship = ShipWaypoint()
        actions = read_actions("./day12/test_input.txt")
        for a in actions:
            ship.take_action(a)
            print(ship.position)
            print(f'waypoint: {ship.waypoint}')
        self.assertEqual(abs(ship.position[0]) + abs(ship.position[1]), 286)
