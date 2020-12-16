import re


def parse_ticket(ticket_str):
    return [int(i) for i in ticket_str.split(",")]


class Rule:

    def __init__(self, name, min1, max1, min2, max2):
        self.name = name
        self.min1 = min1
        self.max1 = max1
        self.min2 = min2
        self.max2 = max2

    @classmethod
    def from_string(cls, rule_str):
        '''
        Parses a rule as a string into a Rule object
        '''
        name = rule_str.split(":")[0]
        numbers = [int(i) for i in re.findall(r'\d+', rule_str)]
        return cls(name, *numbers)

    def check(self, value):
        '''
        Checks whether value respects the rule, returns bool
        '''
        return self.min1 <= value <= self.max1 or \
            self.min2 <= value <= self.max2


class TicketValidator:

    def __init__(self):
        self.rules = []
        self.rules_validity = {}

    def read_rules(self, path):
        '''
        Read rules from file into a list, saved in "rules" attribute
        '''
        with open(path) as f:
            rules = [Rule.from_string(line.strip()) for line in f]
        self.rules = rules

    def get_invalids(self, ticket):
        '''
        Returns the list of invalid fields in tickets (i.e. fields that do not
        check any rule in "rules")
        '''
        invalids = []
        for n in ticket:
            if not any([r.check(n) for r in self.rules]):
                invalids.append(n)
        return invalids

    def _get_rules_validity(self, ticket):
        '''
        Returns a dict, with rules as keys, and as values a set of positions
        (0 indexed) at which the ticket passes the rule check.
        '''

        valid = {}
        for rule in self.rules:
            valid[rule.name] = set()
        for i, n in enumerate(ticket):
            for rule in self.rules:
                if rule.check(n):
                    valid[rule.name].add(i)
        return valid

    def _clean_rules_validity(self):
        '''
        When a set is a singleton, then we know for sure the name of the
        column. This function clears the "rules_validity" attribute so that
        other rules do not consider this column anymore (removes the position
        of the corresponding sets
        '''
        any_update = True  # Update at least once
        while any_update:
            any_update = False
            for rule, s in self.rules_validity.items():
                if len(s) == 1:
                    # we know what field it is
                    # So it cannot be any other
                    element_to_remove = next(iter(s))
                    other_sets = [other_s
                                  for other_rule, other_s
                                  in self.rules_validity.items()
                                  if other_rule != rule]
                    for other_s in other_sets:
                        if element_to_remove in other_s:
                            any_update = True
                            other_s.remove(element_to_remove)

    def update_rules_validity(self, ticket):
        '''
        Updates the "rules_validity" attribute as a dict:
        {"rule name": {set of possible columns concerned}}
        given additinal information in `ticket`.
        '''
        if self.rules_validity == {}:
            self.rules_validity = self._get_rules_validity(ticket)
        else:
            new_validity = self._get_rules_validity(ticket)
            for k, s in self.rules_validity.items():
                s.intersection_update(new_validity[k])
        self._clean_rules_validity()


if __name__ == "__main__":
    tv = TicketValidator()
    tv.read_rules("./day16/rules.txt")
    error_rate = 0
    with open("./day16/nearby_tickets.txt") as f:
        for ticket_str in f:
            ticket = parse_ticket(ticket_str.strip())
            error_rate += sum(tv.get_invalids(ticket))
    print("Solution day16A")
    print(error_rate)

    print()
    my_ticket = [83, 53, 73, 139, 127, 131, 97, 113, 61,
                 101, 107, 67, 79, 137, 89, 109, 103, 59, 149, 71]
    with open("./day16/nearby_tickets.txt") as f:
        for ticket_str in f:
            ticket = parse_ticket(ticket_str.strip())
            if tv.get_invalids(ticket) == []:  # Valid tickets only
                tv.update_rules_validity(ticket)
    solution_B = 1
    for rule in [r for r in tv.rules_validity
                 if re.match("departure", r)]:
        solution_B *= my_ticket[tv.rules_validity[rule].pop()]

    print("Solution day16B")
    print(solution_B)
