from itertools import combinations

def find_combination_given_sum(l, length, expected_sum):
    """
      Finds in a list a combination of values of length "length" for which the
      sum is equal to "expected_sum". Returns the first combination found (in
      ascending order of indexes), or None if none is found
    """
    if len(l) >= length:
        for combination in combinations(l, length):
            if sum(combination) == expected_sum:
                return combination
    return None

def read_input(path):
    with open(path) as f:
        input = [int(line) for line in f]
    return(input)

def print_solution(solution, problem):
    product = 1
    for s in solution:
        product *= s
    print(
        f'Solution {problem}\n'
        f'------------\n'
        f'Sum of {solution} is {sum(solution)}\n'
        f'Product of {solution} is {product}'
    )

if __name__ == '__main__':
    l = read_input("./day1/input.txt")
    sol1a = find_combination_given_sum(l, 2, 2020)
    print_solution(sol1a, "1A")
    sol2a = find_combination_given_sum(l, 3, 2020)
    print_solution(sol2a, "2A")
