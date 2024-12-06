with open('input/6.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        grid[x + y * 1j] = lines[y][x]
        if lines[y][x] == '^':
            initial_guard_position = x + y * 1j

def get_visited_coordinates(obstacle_position):
    guard_position = initial_guard_position
    guard_direction = -1j

    previously_visited_positions = set()
    visited_coordinates = set()

    while guard_position in grid:
        if (guard_position, guard_direction) in previously_visited_positions:
            return set()
        previously_visited_positions.add((guard_position, guard_direction))
        visited_coordinates.add(guard_position)
        next_position = guard_position + guard_direction
        if grid.get(next_position) == '#' or next_position == obstacle_position:
            guard_direction *= 1j
        else:
            guard_position = next_position

    return visited_coordinates

visited_coordinates = get_visited_coordinates(-10)

print("Part 1:", len(visited_coordinates))

loop_positions = 0
for i, c in enumerate(visited_coordinates):
    if i % 100 == 0:
        print(i, "/", len(visited_coordinates))
    if len(get_visited_coordinates(c)) == 0:
        loop_positions += 1
print("Part 2:", loop_positions)