import unittest
from day16.solution_day16 import Rule, TicketValidator, parse_ticket


class TestReadRules(unittest.TestCase):

    def test_read_rule(self):
        actual = Rule.from_string("departure location: 27-840 or 860-957")
        expected = Rule("departure location", 27, 840, 860, 957)
        self.assertEqual(actual.name, expected.name)
        self.assertEqual(actual.min1, expected.min1)
        self.assertEqual(actual.min2, expected.min2)
        self.assertEqual(actual.max1, expected.max1)
        self.assertEqual(actual.max2, expected.max2)

    def test_check_rule(self):
        rule = Rule.from_string("departure location: 27-840 or 860-957")
        true_values = [27, 34, 837, 840, 860, 871, 957]
        false_values = [-7, 12, 27, 841, 850, 859, 958, 1012]
        self.assertTrue(all([rule.check(v) for v in true_values]))
        self.assertFalse(not any([rule.check(v) for v in false_values]))


class TestTicketValidation(unittest.TestCase):

    def test_validate_ticket_1rule(self):
        tv = TicketValidator()
        tv.rules = [Rule.from_string("departure location: 27-840 or 860-957")]
        self.assertEqual(tv.get_invalids([12]), [12])
        self.assertEqual(tv.get_invalids([28]), [])
        self.assertEqual(tv.get_invalids([12, 28]), [12])
        self.assertEqual(
            tv.get_invalids([12, 28, 820, 845, 846]),
            [12, 845, 846]
        )

    def test_validate_ticket(self):
        tv = TicketValidator()
        tv.rules = [
            Rule.from_string("departure location: 27-840 or 860-957"),
            Rule.from_string("price: 1-2, 4-6")
        ]
        self.assertEqual(tv.get_invalids([12]), [12])
        self.assertEqual(tv.get_invalids([28]), [])
        self.assertEqual(tv.get_invalids([2, 3, 5, 28]), [3])
        self.assertEqual(
            tv.get_invalids([1, 12, 28, 820, 845, 846]),
            [12, 845, 846]
        )

    def test_rules_validity(self):
        tv = TicketValidator()
        tv.rules = [
            Rule.from_string("departure location: 27-840 or 860-957"),
            Rule.from_string("price: 1-2, 4-6"),
            Rule.from_string("route: 5-28, 1000-1001")
        ]
        tv.update_rules_validity([2, 5, 28]),
        self.assertEqual(
            tv.rules_validity,
            {"price": {0}, "departure location": {2}, "route": {1}}
        )
        tv.update_rules_validity([2, 27, 800]),
        self.assertEqual(
            tv.rules_validity,
            {"price": {0}, "departure location": {2}, "route": {1}}
        )


class TestSolutionA(unittest.TestCase):

    def test_solutionA(self):
        tv = TicketValidator()
        tv.read_rules("./day16/test_rules.txt")
        error_rate = 0
        with open("./day16/test_nearby_tickets.txt") as f:
            for ticket_str in f:
                ticket = parse_ticket(ticket_str.strip())
                error_rate += sum(tv.get_invalids(ticket))
        self.assertEqual(error_rate, 71)

class TestSolutionB(unittest.TestCase):
    def test_solutionB(self):
        tv = TicketValidator()
        tv.read_rules("./day16/test_rules_B.txt")
        with open("./day16/test_nearby_ticket_B.txt") as f:
            for ticket_str in f:
                ticket = parse_ticket(ticket_str.strip())
                if (tv.get_invalids(ticket) == []):
                    tv.update_rules_validity(ticket)
        self.assertTrue(all([len(s) == 1 for s in tv.rules_validity.values()]))
