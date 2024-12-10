with open('input/10.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[x + y * 1j] = int(char)

trailheads = [key for key, value in grid.items() if value == 0]

def get_score(trailhead, count_distinct_paths=False):
    score = 0
    queue = [trailhead]
    encountered_positions = set()
    while len(queue) > 0:
        position = queue.pop(0)
        if position in encountered_positions:
            continue
        if not count_distinct_paths:
            encountered_positions.add(position)
        elevation = grid[position]
        if elevation == 9:
            score += 1
            continue
        surrounding_positions = [position + direction for direction in [1, -1, 1j, -1j] if position + direction in grid and grid[position + direction] == elevation + 1]
        queue.extend(surrounding_positions)
    return score


print("Part 1:", sum(get_score(trailhead) for trailhead in trailheads))
print("Part 2:", sum(get_score(trailhead, count_distinct_paths=True) for trailhead in trailheads))