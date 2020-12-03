import numpy as np

def read_forest(path):
    """ Reads a forest map at "path" """
    with open(path) as f:
        forest = parse_forest(l.strip() for l in f)
        return(forest)

def parse_forest(lines):
    """
    Parses a forest from a list of row strings into numpy.array of 0s and 1s
    (1 if there is a tree)
    """
    def convert_line_to_int(line):
        tr = str.maketrans(".#", "01")
        return [int(d) for d in line.translate(tr)]
    return np.array([convert_line_to_int(l) for l in lines])

def is_a_tree(forest, coords):
    """
    Check if "coords"  coordinates are trees (list of tuples, first element is
    row, second is column, both 0 indexed) in "forest".
    Returns a list of `bool` of same length as "coords".
    """
    if type(coords) is not list:
        raise ValueError
    if len(coords) == 0:
        raise ValueError
    (forest_depth, forest_width) = forest.shape
    if any([not 0 <= r < forest_depth for r, _ in coords]):
        raise ValueError
    is_a_tree = [forest[r, c % forest_width] == 1 for r, c in coords]
    return is_a_tree

def count_trees_on_way(direction, forest):
    """ Counts trees on way with "direction" a tuple (x, y) """
    max_steps = int(forest.shape[0] / direction[0])
    coords = [(direction[0] * step, direction[1] * step) \
        for step in range(max_steps)]
    return sum(is_a_tree(forest, coords))

if __name__ == "__main__":
    forest = read_forest("./input.txt")
    direction = (1, 3)
    ntrees1A = count_trees_on_way(direction, forest)
    print(
        f'Problem 3A:\n'
        f'-----------\n'
        f'Number of trees in direction {direction}: {ntrees1A}'
        )

    print()
    possible_directions = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    result1B = 1
    for direction in possible_directions:
        result1B *= count_trees_on_way(direction, forest)
    print(
        f'Problem 3B:\n'
        f'-----------\n'
        f'Solution: {result1B}'
        )

