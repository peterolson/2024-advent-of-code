with open('input/15.txt', 'r') as f:
    grid_text, moves = f.read().split("\n\n")

grid = {}
for y, row in enumerate(grid_text.split("\n")):
    for x, cell in enumerate(row):
        location = x + y * 1j
        grid[location] = cell
        if cell == "@":
            roboot_location = location

movemap = {
    ">": 1,
    "<": -1,
    "^": -1j,
    "v": 1j
}

def perform_move(grid, roboot_location, move):
    new_location = roboot_location + movemap[move]
    boxes_to_push = []
    while grid[new_location] == "O":
        new_location = new_location + movemap[move]
        boxes_to_push.append(new_location)

    if grid[new_location] == "#":
        return roboot_location
    if grid[new_location] == ".":
        for box in boxes_to_push:
            grid[box] = "O"
        grid[roboot_location] = "."
        roboot_location = roboot_location + movemap[move]
        grid[roboot_location] = "@"
        return roboot_location

def get_coord(position):
    return int(position.imag) * 100 + int(position.real)

def print_grid(grid, grid_text):
    for y in range(grid_text.count("\n") + 1):
        for x in range(len(grid_text.split("\n")[0])):
            print(grid.get(x + y * 1j, " "), end="")
        print()

for move in "".join(moves.split()):
    roboot_location = perform_move(grid, roboot_location, move)

box_coord_sum = sum([get_coord(position) for position, cell in grid.items() if cell == "O"])
print("Part 1:", box_coord_sum)

widened_grid_text = grid_text.replace("#","##").replace("O", "[]").replace(".", "..").replace("@", "@.")
grid = {}
for y, row in enumerate(widened_grid_text.split("\n")):
    for x, cell in enumerate(row):
        location = x + y * 1j
        grid[location] = cell
        if cell == "@":
            roboot_location = location


def perform_move(grid, roboot_location, move):
    if grid[roboot_location + move] == "#":
        return roboot_location
    
    locations_to_push_from = [roboot_location]
    boxes_to_push = []

    while any([grid[location + move] in "[]" for location in locations_to_push_from]):
        if any([grid[location + move] == "#" for location in locations_to_push_from]):
            return roboot_location
        new_locations_to_push_from = []
        for location in locations_to_push_from:
            boxes = []
            if grid[location + move] == "[":
                boxes = [location + move]
                if move in [1j, -1j]:
                    boxes.append(location + move + 1)
            elif grid[location + move] == "]":
                boxes = [location + move]
                if move in [1j, -1j]:
                    boxes.append(location + move - 1)
            boxes_to_push.extend(boxes)
            new_locations_to_push_from.extend(boxes)
        locations_to_push_from = new_locations_to_push_from

    if any([grid[box+move] == "#" for box in boxes_to_push]):
        return roboot_location

    new_symbols = {}
    for box in boxes_to_push:
        symbol = grid[box]
        new_symbols[box + move] = symbol
    for box in boxes_to_push:
        grid[box] = "."
    for box, symbol in new_symbols.items():
        grid[box] = symbol

    grid[roboot_location] = "."
    roboot_location = roboot_location + move
    grid[roboot_location] = "@"
    return roboot_location

for move in "".join(moves.split()):
    roboot_location = perform_move(grid, roboot_location, movemap[move])

box_coord_sum = sum([get_coord(position) for position, cell in grid.items() if cell == "["])
print("Part 2:", box_coord_sum)