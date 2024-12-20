from collections import Counter


with open('input/20.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        position = j + i * 1j
        grid[position] = char
        if char == 'S':
            start_position = position
        if char == 'E':
            end_position = position

def get_distances_from_end(grid):
    distances = {}
    distances[end_position] = 0
    queue = [end_position]
    while queue:
        position = queue.pop(0)
        for direction in [1, -1, 1j, -1j]:
            new_position = position + direction
            if new_position not in grid:
                continue
            if new_position in distances:
                continue
            if grid[new_position] == '#':
                continue
            distances[new_position] = distances[position] + 1
            queue.append(new_position)
    return distances

distances_from_end = get_distances_from_end(grid)

time_without_cheating = distances_from_end[start_position]

wall_positions = {position for position, char in grid.items() if char == '#'}
time_savings = {}

for position in wall_positions:
    adjacent_positions = [position + direction for direction in [1, -1, 1j, -1j] if position + direction in grid and grid[position + direction] != '#']
    if len(adjacent_positions) == 0:
        continue
    min_distance = min([distances_from_end[adjacent_position] for adjacent_position in adjacent_positions])
    for adjacent_position in adjacent_positions:
        time_from_position = min([distances_from_end[adjacent_position], min_distance + 2])
        time_savings[(position, adjacent_position)] = distances_from_end[adjacent_position] - time_from_position

count = 0
for (position, adjacent_position), time_saved in time_savings.items():
    if time_saved >= 100:
        count += 1
print("Part 1:", count)

def distance(position1, position2):
    return int(abs(position1.real - position2.real) + abs(position1.imag - position2.imag))

def count_cheats(cheat_length):
    cheats = {}
    for i, start_position in enumerate(distances_from_end):
        if i % 100 == 0:
            print(i, "of", len(distances_from_end))
        end_positions = [e for e in distances_from_end if distance(start_position, e) <= cheat_length and distances_from_end[e] < distances_from_end[start_position]]
        for end_position in end_positions:
            time_saved = distances_from_end[start_position] - distances_from_end[end_position] - distance(start_position, end_position)
            if (start_position, end_position) not in cheats:
                cheats[(start_position, end_position)] = time_saved
            elif time_saved < cheats[(start_position, end_position)]:
                cheats[(start_position, end_position)] = time_saved

    cheats_by_time = Counter()
    for cheat in cheats:
        cheats_by_time[cheats[cheat]] += 1
    return cheats_by_time

print("Part 2:", sum([c for s, c in count_cheats(20).items() if s >= 100]))




