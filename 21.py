from functools import cache
from itertools import permutations

with open('input/21.txt', 'r') as f:
    lines = f.read().splitlines()

num_keypad = ['789', '456', '123', ' 0A']
arrow_keypad = [' ^A', '<v>']
directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

transitions = {}

num_coords = {}
for y, row in enumerate(num_keypad):
    for x, key in enumerate(row):
        if key != " ":
            num_coords[key] = (x, y)

arrow_coords = {}
for y, row in enumerate(arrow_keypad):
    for x, key in enumerate(row):
        if key != " ":
            arrow_coords[key] = (x, y)

@cache
def count_presses(sequence, depth, start='A'):
    if len(sequence) == 0:
        return 0
    end = sequence[0]
    coords = arrow_coords if start in arrow_coords and end in arrow_coords else num_coords
    x0, y0 = coords[start]
    x1, y1 = coords[end]
    dx, dy = x1 - x0, y1 - y0
    x_arrow = ">" if dx > 0 else "<"
    y_arrow = "v" if dy > 0 else "^"
    buttons_to_press = x_arrow * abs(dx) + y_arrow * abs(dy)

    if depth == 0:
        return len(buttons_to_press) + 1 + count_presses(sequence[1:], depth, end)
    
    valid_orders = []
    for button_order in set(permutations(buttons_to_press)):
        x0, y0 = coords[start]
        is_valid = True
        for button in button_order:
            dx, dy = directions[button]
            x0 += dx
            y0 += dy
            if (x0, y0) not in coords.values():
                is_valid = False
                break
        if is_valid:
            valid_orders.append(''.join(button_order))
    min_presses = min(count_presses(button_order + 'A', depth - 1) for button_order in valid_orders)
    return min_presses + count_presses(sequence[1:], depth, end)

def get_complexity(code, depth):
    n = int(code.lstrip('0').replace('A', ''))
    return count_presses(code, depth) * n

print("Part 1:", sum(get_complexity(line, 2) for line in lines))
print("Part 2:", sum(get_complexity(line, 25) for line in lines))