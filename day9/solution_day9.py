import numpy as np


def read_input(path):
    with open(path) as f:
        return np.array([int(li.strip()) for li in f])


def is_sum_of_two(row_id, last_n, array):
    """ Checks if row_id is the sum of two numbers in last_n """
    subarray = array[(row_id-last_n):row_id]
    pair_sums = subarray[:, np.newaxis] + subarray
    candidates = pair_sums[np.triu_indices_from(pair_sums, k=1)]
    if array[row_id] in candidates:
        return True
    else:
        return False


def find_contiguous_sum_equal_to(number, array):
    """
    Finds a contiguous range in "array" which sum is equal to "number"
    Returns the values inside this range.
    """
    for i in range(0, len(array)):
        contiguous_sum = 0
        n_contiguous = 0
        while contiguous_sum <= number and i + n_contiguous < len(array):
            contiguous_sum += array[i + n_contiguous]
            if contiguous_sum == number:
                return array[i:(i + n_contiguous + 1)]
            n_contiguous += 1


if __name__ == "__main__":
    array = read_input("./day9/input.txt")
    last_n = 25
    for i in range(last_n, len(array)):
        if not is_sum_of_two(i, last_n, array):
            solution9A = array[i]
            break

    print("Solution 9A")
    print("-----------")
    print(solution9A)
    print()

    contiguous = find_contiguous_sum_equal_to(solution9A, array)
    solution9B = min(contiguous) + max(contiguous)
    print("Solution 9B")
    print("-----------")
    print(solution9B)
