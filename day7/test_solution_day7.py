import unittest
from day7.solution_day7 import (parse_rule, read_rules, find_containers,
                                count_bags)

class ParseRule(unittest.TestCase):

    def test_parse_rule(self):
        rules = [
            'light red bags contain 1 bright white bag, 2 muted yellow bags.',
            'bright white bags contain 1 shiny gold bag.',
            'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
            'dotted black bags contain no other bags.'
        ]
        actual = [parse_rule(r) for r in rules]
        expected = [
            {'light red': {'bright white': 1, 'muted yellow': 2}},
            {'bright white': {'shiny gold': 1}},
            {'dark olive': {'faded blue': 3, 'dotted black': 4}},
            {'dotted black': {}}
        ]
        self.assertEqual(actual, expected)

    def test_read_rules(self):
        actual = read_rules('./day7/test_input.txt')
        self.assertEqual(actual['faded blue'], {})
        self.assertEqual(
            actual['vibrant plum'],
            {'faded blue': 5, 'dotted black': 6}
        )
        self.assertEqual(
            actual['bright white'],
            {'shiny gold': 1}
        )

class TestFindContainers(unittest.TestCase):

    def test_find_containers(self):
        rules = read_rules('./day7/test_input.txt')
        actual = find_containers("shiny gold", rules)
        expected = {
            "bright white",
            "muted yellow",
            "dark orange",
            "light red"
        }
        self.assertEqual(actual, expected)

class TestCountBags(unittest.TestCase):

    def test_count_bags(self):
        rules = read_rules('./day7/test_input.txt')
        actual = count_bags("shiny gold", rules)
        expected = 32
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
