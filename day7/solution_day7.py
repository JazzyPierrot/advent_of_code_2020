import re

def parse_rule(rule):
    digits = [int(d) for d in re.findall("\d", rule)]
    n_bag_types = len(digits)
    rule_splitted = str.split(rule, " ")
    col_container = " ".join(rule_splitted[:2])
    parsed_rule = {col_container: {}}
    for i, d in enumerate(digits):
        parsed_rule[col_container][" ".join(rule_splitted[5 + 4 * i:7 + 4 * i])] = d
    return parsed_rule

def read_rules(path):
    rules = {}
    with open(path) as f:
        for l in f:
            rules.update(parse_rule(l))
    return rules
