from math import sin, cos, acos, pi, sqrt


def parse_action(action_string):
    return (action_string[0], int(action_string[1:]))


def read_actions(path):
    with open(path) as f:
        return [parse_action(a.strip()) for a in f]


def cart2pol(coordinates):
    r = sqrt(coordinates[0] ** 2 + coordinates[1] ** 2)
    if coordinates[1] >= 0:
        theta = acos(coordinates[0] / r)
    else:
        theta = - acos(coordinates[0] / r)
    return (r, theta)


def pol2cart(pol):
    return (round(pol[0] * cos(pol[1]), ndigits=3), round(pol[0] * sin(pol[1]), ndigits=3))


class Ship:

    def __init__(self):
        self.position = [0, 0]
        self.direction = [1, 0]

    def take_action(self, action):

        if action[0] == "F":
            self.position = [p + action[1] * d
                             for p, d in zip(self.position, self.direction)]

        elif action[0] == "E":
            self.position[0] += action[1]
        elif action[0] == "W":
            self.position[0] -= action[1]
        elif action[0] == "N":
            self.position[1] += action[1]
        elif action[0] == "S":
            self.position[1] -= action[1]

        elif action[0] == "L":
            theta = cart2pol(self.direction)[1]
            theta += action[1] * pi / 180
            self.direction = list(pol2cart((1, theta)))
        elif action[0] == "R":
            theta = cart2pol(self.direction)[1]
            theta -= action[1] * pi / 180
            self.direction = list(pol2cart((1, theta)))


class ShipWaypoint:

    def __init__(self):
        self.position = [0, 0]
        self.waypoint = [10, 1]

    def take_action(self, action):

        if action[0] == "F":
            self.position = [p + action[1] * d
                             for p, d in zip(self.position, self.waypoint)]

        elif action[0] == "E":
            self.waypoint[0] += action[1]
        elif action[0] == "W":
            self.waypoint[0] -= action[1]
        elif action[0] == "N":
            self.waypoint[1] += action[1]
        elif action[0] == "S":
            self.waypoint[1] -= action[1]

        elif action[0] == "L":
            pol = cart2pol(self.waypoint)
            new_pol = (pol[0], pol[1] + action[1] * pi / 180)
            self.waypoint = list(pol2cart(new_pol))
        elif action[0] == "R":
            pol = cart2pol(self.waypoint)
            new_pol = (pol[0], pol[1] - action[1] * pi / 180)
            self.waypoint = list(pol2cart(new_pol))


if __name__ == "__main__":

    actions = read_actions("./day12/input.txt")

    ship = Ship()
    for a in actions:
        ship.take_action(a)
    solution12A = abs(ship.position[0]) + abs(ship.position[1])
    print(solution12A)

    ship = ShipWaypoint()
    for a in actions:
        ship.take_action(a)
    solution12B = abs(ship.position[0]) + abs(ship.position[1])
    print(solution12B)
