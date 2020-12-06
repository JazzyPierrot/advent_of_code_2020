from common.aoc_functions import split_batch

def read_unique_answers(path):
    """
    Read batch/group answers at path and returns a list of set of unique answers
    (one set for each group)
    """
    with open(path) as f:
        return([set(t.replace(';','')) for t in split_batch(f, ';')])

def read_common_answers(path):
    """
    Read batch/group answers at path and returns a list of set of common answers
    (one set for each group)
    """
    res = []
    with open(path) as f:
        for l in split_batch(f, ';'):
            answer_sets = [set(a) for a in l.split(";")]
            res.append(set.intersection(*answer_sets))
        return res

if __name__ == "__main__":
    unique_answers = read_unique_answers("./day6/input.txt")
    solution6A = sum(len(a) for a in unique_answers)
    print("Solution A:")
    print("-----------")
    print(f"Sum of unique answers: {solution6A}")
    common_answers = read_common_answers("./day6/input.txt")
    solution6B = sum(len(a) for a in common_answers)
    print("Solution B:")
    print("-----------")
    print(f"Sum of common answers: {solution6B}")
