import itertools

class EnergyGrid:

    def __init__(self, path):
        self.map = set()
        with open(path) as f:
            for i, line in enumerate(f):
                for j, character in enumerate(line.strip()):
                    if character == '#':
                        self.map.add((i, j, 0))

    def get_adjacent_squares(self, pos):
        assert len(pos) == 3, "Position must be 3 dimensional"
        relative_pos = [k for k in itertools.product([-1, 0, 1], repeat = 3) if k != (0, 0, 0)]
        assert len(relative_pos) == 26
        adjacent_pos = [ (pos[0] + a, pos[1] + b, pos[2] + c) for a, b, c in relative_pos ]
        return adjacent_pos

    def get_active_adjacency_map(self):
        active_adjacent = {}
        for active in self.map:
            adjs = self.get_adjacent_squares(active)
            for adj in adjs:
                active_adjacent[adj] = active_adjacent.get(adj, 0) + 1
        return active_adjacent

    def update_map(self):
        new_map = set()
        active_adjacent = self.get_active_adjacency_map()
        interesting_pos = self.map.union(active_adjacent.keys())
        for pos in interesting_pos:
            if pos in self.map and pos in active_adjacent and (active_adjacent[pos] == 2 or active_adjacent[pos] == 3):
                new_map.add(pos)
            if (not pos in self.map) and pos in active_adjacent and active_adjacent[pos] == 3:
                new_map.add(pos)
        self.map = new_map

    def count_active_cycle6(self):
        for _ in range(0, 6):
            self.update_map()
        return len(self.map)

class EnergyHyperGrid:

    def __init__(self, path):
        self.map = set()
        with open(path) as f:
            for i, line in enumerate(f):
                for j, character in enumerate(line.strip()):
                    if character == '#':
                        self.map.add((i, j, 0, 0))

    def get_adjacent_squares(self, pos):
        assert len(pos) == 4, "Position must be 4 dimensional"
        relative_pos = [k for k in itertools.product([-1, 0, 1], repeat = 4) if k != (0, 0, 0, 0)]
        assert len(relative_pos) == 80
        adjacent_pos = [ (pos[0] + a, pos[1] + b, pos[2] + c, pos[3] + d) for a, b, c, d in relative_pos ]
        return adjacent_pos

    def get_active_adjacency_map(self):
        active_adjacent = {}
        for active in self.map:
            adjs = self.get_adjacent_squares(active)
            for adj in adjs:
                active_adjacent[adj] = active_adjacent.get(adj, 0) + 1
        return active_adjacent

    def update_map(self):
        new_map = set()
        active_adjacent = self.get_active_adjacency_map()
        interesting_pos = self.map.union(active_adjacent.keys())
        for pos in interesting_pos:
            if pos in self.map and pos in active_adjacent and (active_adjacent[pos] == 2 or active_adjacent[pos] == 3):
                new_map.add(pos)
            if (not pos in self.map) and pos in active_adjacent and active_adjacent[pos] == 3:
                new_map.add(pos)
        self.map = new_map

    def count_active_cycle6(self):
        for _ in range(0, 6):
            self.update_map()
        return len(self.map)

if __name__ == "__main__":
    eg = EnergyGrid("./day17/input.txt")
    print(eg.count_active_cycle6())

    ehg = EnergyHyperGrid("./day17/input.txt")
    print(ehg.count_active_cycle6())
