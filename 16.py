import heapq

with open('input/16.txt', 'r') as f:
    lines = f.read().splitlines()

grid = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        s = lines[i][j]
        position = j + i * 1j
        if s == "#":
            grid[position] = "#"
        else:
            grid[position] = "."
        if s == "S":
            start_position = position
        if s == "E":
            end_position = position

initial_direction = 1

def search_maze(grid, start_position, initial_direction, end_position):
    encountered_positions = set()
    queue = [(0, 0, start_position, initial_direction)]
    counter = 0
    while len(queue) > 0:
        cost, _n, position, direction = heapq.heappop(queue)
        if grid.get(position, "#") == "#":
            continue
        if (position, direction) in encountered_positions:
            continue
        encountered_positions.add((position, direction))
        if position == end_position:
            return cost
        
        counter += 1
        heapq.heappush(queue, (cost + 1, counter, position + direction, direction))
        counter += 1
        heapq.heappush(queue, (cost + 1000, counter, position, direction * 1j))
        counter += 1
        heapq.heappush(queue, (cost + 1000, counter, position, direction * -1j))
    return None


print("Part 1:", search_maze(grid, start_position, initial_direction, end_position))

MAX_INT = 2 ** 31 - 1

def tiles_on_best_paths(grid, start_position, initial_direction, end_position):
    encountered_costs = {}
    queue = [(0, 0, start_position, initial_direction, set([start_position]))]
    counter = 0
    best_solution = MAX_INT
    visited_positions_on_best_solution = set()
    while len(queue) > 0:
        cost, _n, position, direction, visited_positions = heapq.heappop(queue)
        if grid.get(position, "#") == "#":
            continue
        if encountered_costs.get((position, direction), MAX_INT) < cost:
            continue
        encountered_costs[(position, direction)] = cost
        if position == end_position:
            if cost <= best_solution:
                best_solution = cost
                visited_positions_on_best_solution |= visited_positions
            if cost > best_solution:
                break
        
        counter += 1
        heapq.heappush(queue, (cost + 1, counter, position + direction, direction, visited_positions | set([position + direction])))
        counter += 1
        heapq.heappush(queue, (cost + 1000, counter, position, direction * 1j, visited_positions))
        counter += 1
        heapq.heappush(queue, (cost + 1000, counter, position, direction * -1j, visited_positions))
    return len(visited_positions_on_best_solution)

print("Part 2:", tiles_on_best_paths(grid, start_position, initial_direction, end_position))