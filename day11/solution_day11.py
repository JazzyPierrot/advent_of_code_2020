import numpy as np
import itertools


def parse_input(txt):
    ''' Parses a input iterable other lines into a numpy.array '''
    array_list = [[char for char in line.strip()] for line in txt]
    return(np.array(array_list))


def read_input(path):
    ''' Reads file at 'path' and parse input to a numpy.array '''
    with open(path) as f:
        return parse_input(f.readlines())


class AdjacentMap:
    ''' Find and save adjacent seats for a given coordinate '''

    def __init__(self, initial_grid):
        self.initial_grid = initial_grid
        self.memory = {}  # Do not repeat computations

    def get_adjacent_coords(self, coord):
        '''
        Get coordinates of the adjacent seats to the coordinates 'coord'
        on the grid
        '''
        if coord in self.memory:
            return self.memory[coord]
        i_rge = range(
            max(coord[0] - 1, 0),
            min(coord[0] + 2, self.initial_grid.shape[0])
        )
        j_rge = range(
            max(coord[1] - 1, 0),
            min(coord[1] + 2, self.initial_grid.shape[1])
        )
        adjacent_seats = [(i, j)
                          for i, j in itertools.product(i_rge, j_rge)
                          if (i, j) != coord
                          and self.initial_grid[i, j] != "."]
        self.memory[coord] = adjacent_seats
        return adjacent_seats

    def n_adjacent_occupied(self, coord, grid):
        '''
        Counts the number of occupied seats adjacent to "coord" on "grid"
        '''
        assert len(coord) == 2, "coord should be a coordinate tuple of size 2"
        adjacent = self.get_adjacent_coords(coord)
        return sum([grid[adj] == "#" for adj in adjacent])


class AdjacentSightMap(AdjacentMap):
    '''
    Find and save adjacent seats for a given coordinate with new
    definition: adjacent = in sight
    '''

    def _coord_inside_grid(self, coord):
        ''' Return wether 'coord' is a valid index '''
        return 0 <= coord[0] < self.initial_grid.shape[0] and \
            0 <= coord[1] < self.initial_grid.shape[1]

    def _get_new_seat_in_direction(self, coord, direction):
        '''
        Return the first seat in sight (11B definition of "adjacent") from
        'coord' looking in 'direction' (x, y)
        '''
        coord_observed = coord
        observed = "."
        while observed != "L":
            coord_observed = tuple(a + b for a, b in zip(coord, direction))
            if (not self._coord_inside_grid(coord_observed)):
                raise IndexError
            coord = coord_observed
            observed = self.initial_grid[coord_observed]
        return coord_observed

    def get_adjacent_coords(self, coord):
        '''
        Get the coordinates of seats in sight from "coord"
        '''
        if coord in self.memory:
            return self.memory[coord]
        directions = [d for d in itertools.product((-1, 0, 1), (-1, 0, 1))
                      if d != (0, 0)]
        adjacent_seats = []
        for d in directions:
            try:
                adjacent_seats.append(
                    self._get_new_seat_in_direction(coord, d)
                )
            except IndexError:
                next
        self.memory[coord] = adjacent_seats
        return adjacent_seats


def update_grid(grid, adjacent_map, thres_leav=4):
    '''
    Update the grid, given the adjacent map, and with people starting to
    leave if surrounded by at least "thres_leav" people
    '''
    updated_grid = np.full(grid.shape, ".")
    for coord in itertools.product(
        range(0, grid.shape[0]),
            range(0, grid.shape[1])
    ):
        if grid[coord] == "L" and \
                adjacent_map.n_adjacent_occupied(coord, grid) == 0:
            updated_grid[coord] = "#"
        elif grid[coord] == "#" and \
                adjacent_map.n_adjacent_occupied(coord, grid) >= thres_leav:
            updated_grid[coord] = "L"
        else:
            updated_grid[coord] = grid[coord]
    return(updated_grid)


def update_to_stationnarity(grid, adjacent_map, thres_leav=4):
    '''
    Repeatedly update the grid until it is stationnary
    '''
    updated_grid = update_grid(grid, adjacent_map, thres_leav)
    while (updated_grid != grid).any():
        grid = updated_grid
        updated_grid = update_grid(grid, adjacent_map, thres_leav)
    return grid


if __name__ == "__main__":
    grid = read_input("./day11/input.txt")
    adjacent_map = AdjacentMap(grid)
    grid = update_to_stationnarity(grid, adjacent_map, 4)
    solution11A = (grid == "#").sum()
    print(solution11A)
    print()

    grid = read_input("./day11/input.txt")
    adjacent_map = AdjacentSightMap(grid)
    grid = update_to_stationnarity(grid, adjacent_map, 5)
    solution11B = (grid == "#").sum()
    print(solution11B)
