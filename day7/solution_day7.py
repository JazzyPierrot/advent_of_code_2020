import re

def parse_rule(rule):
    """
    Parse a rule based on word order and number of digits found in the
    rule. Returns a dictionary `{containing color: {contained color 1: #,
    ...}}`
    """
    digits = [int(d) for d in re.findall("\d", rule)]
    n_bag_types = len(digits)
    rule_splitted = str.split(rule, " ")
    col_container = " ".join(rule_splitted[:2])
    parsed_rule = {col_container: {}}
    for i, d in enumerate(digits):
        parsed_rule[col_container][" ".join(rule_splitted[5 + 4 * i:7 + 4 * i])] = d
    return parsed_rule

def read_rules(path):
    """
    Read rules from file, parse them and return a dictionary of all rules.
    """
    rules = {}
    with open(path) as f:
        for l in f:
            rules.update(parse_rule(l))
    return rules

def find_containers(color, rules):
    """
    Find colors of bag that can contain a bag of color "color", according to
    "rules"
    """
    containers = set()
    for c in rules:
        if color in rules[c]:
            if c not in containers:
                containers.add(c)
                containers.update(find_containers(c, rules))
    return containers

def count_contained_bags(color, rules, counts_aux = {}):
    """
    Count the number of contained bags inside a bag of color "color",
    according to "rules".
    "counts_aux" is only for performance, avoiding recomputing the count for a
    color already met before.
    """
    n_in_color = 0
    for c in rules[color]:
        n_c_in_color = rules[color][c]
        n_in_color += n_c_in_color
        if c not in counts_aux:
            counts_aux[c] = count_contained_bags(c, rules, counts_aux)
        n_in_c = counts_aux[c]
        n_in_color += n_c_in_color * n_in_c
    return n_in_color

if __name__ == "__main__":
    rules = read_rules("./day7/input.txt")
    color = "shiny gold"
    solution7A = find_containers(color, rules)
    print("Solution 7A")
    print("-----------")
    print(f"A bag of color {color} may be contained inside {len(solution7A)} other bags")
    print()
    solution7B = count_contained_bags(color, rules)
    print("Solution 7B")
    print("-----------")
    print(f"A bag of color {color} must contain {solution7B} other bags")

