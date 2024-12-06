with open('input/6.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[x + y * 1j] = lines[y][x]
        if lines[y][x] == '^':
            initial_guard_position = x + y * 1j

def count_visited_positions(obstacle_position):
    guard_position = initial_guard_position
    guard_direction = -1j

    previously_visited_positions = set()
    visited_coordinates = set()

    while guard_position in grid:
        if (guard_position, guard_direction) in previously_visited_positions:
            return -1
        previously_visited_positions.add((guard_position, guard_direction))
        visited_coordinates.add(guard_position)
        next_position = guard_position + guard_direction
        if grid.get(next_position) == '#' or next_position == obstacle_position:
            guard_direction *= 1j
        else:
            guard_position = next_position

    return len(visited_coordinates)

print("Part 1:", count_visited_positions(-10))

loop_positions = 0
for y in range(len(lines)):
    print(y, "/", len(lines))
    for x in range(len(lines[y])):
        if count_visited_positions(x + y * 1j) == -1:
            loop_positions += 1

print("Part 2:", loop_positions)