def input():
    """
    Returns problems initial numbers
    """
    initial = {}
    for i, n in enumerate((2, 1, 10, 11, 0, 6)):
        initial[n] = i + 1  # 1 indexed
    return initial


def next_step(prev_state, last, step_number):
    """
    Computes the next number, given:
        prev_state: state_dict at step_number - 1 => {number: last_step_seen}
        last: number at step_number
        step_number: current step_number
    returns: (state at step_number, number at step_number + 1)
    """
    if last in prev_state:
        new_last = step_number - prev_state[last]
    else:
        new_last = 0
    prev_state[last] = step_number
    return (prev_state, new_last)


def number_at_step(initial, n):
    """
    Returns number at step n
    """
    last = max(initial, key=initial.get)
    initial_step_number = initial[last]
    del initial[last]
    prev_state = initial
    for step_number in range(initial_step_number, n):
        prev_state, last = next_step(prev_state, last, step_number)
    return last


if __name__ == "__main__":
    print("Solution15A")
    print(number_at_step(input(), 2020))
    print("Solution15B")
    print("brute force")
    print(number_at_step(input(), 30000000))
