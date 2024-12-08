with open('input/8.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        grid[i + j * 1j] = lines[i][j]

antenna_locations = {}
for key, value in grid.items():
    if value != '.':
        if value not in antenna_locations:
            antenna_locations[value] = []
        antenna_locations[value].append(key)

def get_antinodes_pair(a,b):
    diff = b - a
    return [a - diff, b + diff]

def get_unique_antinodes(pair_fn):
    antinode_locations = set()
    for key, locations in antenna_locations.items():
        for i in range(len(locations)):
            for j in range(i + 1, len(locations)):
                antinodes = pair_fn(locations[i], locations[j])
                antinodes = [antinode for antinode in antinodes if antinode in grid]
                antinode_locations.update(antinodes)
    return len(antinode_locations)

print("Part 1:", get_unique_antinodes(get_antinodes_pair))

def get_resonant_antinodes(a,b):
    antinodes = []
    for i in range(-len(lines), len(lines)):
        antinode = a + i * (b - a)
        if antinode in grid:
            antinodes.append(antinode)
    return antinodes

print("Part 2:", get_unique_antinodes(get_resonant_antinodes))