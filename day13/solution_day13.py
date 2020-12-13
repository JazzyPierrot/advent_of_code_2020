import numpy as np


def read_bus_times(path):
    with open(path) as f:
        buses = f.read().strip().split(",")
        buses = [int(b) for b in buses if b != "x"]
        return np.array(buses)


def read_expected_waiting_times(path):
    with open(path) as f:
        buses = f.read().strip().split(",")
        exp = [i + 1 for i, b in enumerate(buses) if b != "x"]
        return np.array(exp)


def get_waiting_times(timestamp, bus_times):
    return bus_times - timestamp % bus_times


def first_available_bus(timestamp, bus_times):
    waiting_time = get_waiting_times(timestamp, bus_times)
    min_waiting_time = waiting_time.min()
    return (bus_times[waiting_time == min_waiting_time], min_waiting_time)


def bezout_aux(r, u, v, rp, up, vp):
    if rp == 0:
        return (r, u, v)
    else:
        div = int(r / rp)
        return bezout_aux(
            rp,
            up,
            vp,
            r - div * rp,
            u - div * up,
            v - div * vp
        )


def bezout(a, b):
    return bezout_aux(a, 1, 0, b, 0, 1)


def get_aligned_waiting_times(bus_times, expected_waittimes):
    # Bus arriving "modulo" minutes before n
    # If bus {bus_times[i]} arrives {modulos[i]} minutes before n,
    # the bus will also be arriving at {expected_waittimes[i]}
    modulos = bus_times - expected_waittimes % bus_times
    for i, _ in enumerate(bus_times):
        prod = int(bus_times[0])
        solution = int(modulos[0])
        for i, bt in enumerate(bus_times[1:]):
            # numpy.int64 leads to overflow
            bt = int(bt)
            new_prod = prod * bt
            s = bezout(prod, bt)
            solution = (solution * s[2] * bt +
                        int(modulos[i+1]) * s[1] * prod) % new_prod
            prod = new_prod
    # Dunno why I systematically underestimate the solution by 1
    return solution + 1


if __name__ == "__main__":
    timestamp = 1000052
    bt = read_bus_times("./day13/input.txt")
    solution13A = first_available_bus(timestamp, bt)
    print("Solution 13A:")
    print(solution13A[0] * solution13A[1])
    print()

    path = "./day13/input.txt"
    bt = read_bus_times(path)
    exp = read_expected_waiting_times(path)
    print("Solution 13B:")
    print(get_aligned_waiting_times(bt, exp))
