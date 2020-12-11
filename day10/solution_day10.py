import numpy as np


def read_input(path):
    with open(path) as f:
        return np.array([int(l.strip()) for l in f])


def differences(vect):
    vect.sort()
    vect_lag = vect.copy()
    vect_lag = np.insert(vect_lag, 0, 0)
    vect = np.append(vect, vect[-1] + 3)
    diff = vect - vect_lag
    return(diff)


def unique_counts(adapters):
    diff = differences(adapters)
    return(np.unique(diff, return_counts=True))


def n_arrangements(adapters):
    ''' Computes the number of arrangements for adapters '''
    diff = differences(adapters)
    return n_arrangements_aux(diff, 0, 3, {})


def n_arrangements_aux(diff, index, max_joltage_gap, memory):
    ''' Looks recursively how many arrangements can be made, given all
    adapters from "index" to the end, and with "max_joltage_gap" (1, 2, or 3)
    to make a valid adapters chain. "diff" are the voltage gaps between
    successive adapters, and memory stores intermediate results to avoid
    recomputations.
    '''
    if max_joltage_gap < diff[index]:
        # The difference in joltage is too important to make a valid chain
        return 0
    elif index == len(diff) - 1:
        # End of the chain, only one possible arrangement
        return 1
    elif (index, max_joltage_gap) in memory:
        # Do not compute twice the same call
        return memory[(index, max_joltage_gap)]
    else:
        # We can choose to pick adapter at index
        n_arr = n_arrangements_aux(diff, index + 1, 3, memory)
        # Or if the gap is not too big (which is checked in the recursive
        # call) we can try not to pick adapter at index
        n_arr += n_arrangements_aux(
            diff,
            index + 1,
            max_joltage_gap - diff[index],
            memory
        )
        # Update memory
        memory[(index, max_joltage_gap)] = n_arr
    return n_arr


if __name__ == "__main__":
    jolts = read_input("./day10/input.csv")
    counts = unique_counts(jolts)
    solution10A = counts[1][0] * counts[1][1]
    print(solution10A)

    print(n_arrangements(jolts))
