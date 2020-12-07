def decode_seat_id(seat):
    """Decodes a seat string into seat_id"""
    bin_seat = seat.translate(str.maketrans("RLBF", "1010"))
    seat_id = int(bin_seat, 2)
    return seat_id

def read_seat_ids(path):
    """ Reads in file many seat_strings and returns a list of seat_strings """
    with open(path) as f:
        return [decode_seat_id(l.strip()) for l in f]

def first_missing_seat_id(seat_ids):
    """ Returns the first missing seat_id in a list of seat_ids """
    for s_id in range(min(seat_ids), max(seat_ids)):
        if s_id not in seat_ids:
            return s_id

if __name__ == "__main__":
    seat_ids = read_seat_ids("./day5/input.txt")
    solution5A = max(seat_ids)
    print(
            f'Solution 5A:\n'
            f'------------\n'
            f'Max seat id: {solution5A}'
    )
    print()
    solution5B = first_missing_seat_id(seat_ids)
    print(
            f'Solution 5B:\n'
            f'------------\n'
            f'Missing seat id: {solution5B}'
            )


