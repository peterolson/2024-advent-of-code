from collections import Counter


with open('input/21.txt', 'r') as f:
    lines = f.read().splitlines()

num_keypad = ['789', '456', '123', ' 0A']
arrow_keypad = [' ^A', '<v>']
directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

transitions = {}

arrow_priority = ["<", "v", ">", "^"]

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

def populate_transitions(coords : dict[str, tuple[int, int]]):
    for a_key, a_coord in coords.items():
        for b_key, b_coord in coords.items():
            if a_key == b_key:
                transitions[(a_key, b_key)] = ""
                continue
            dx, dy = b_coord[0] - a_coord[0], b_coord[1] - a_coord[1]
            x_arrow = ">" if dx > 0 else "<"
            y_arrow = "v" if dy > 0 else "^"
            if dx == 0 and dy == 0:
                transitions[(a_key, b_key)] = ""
            elif dx == 0:
                transitions[(a_key, b_key)] = y_arrow * abs(dy)
            elif dy == 0:
                transitions[(a_key, b_key)] = x_arrow * abs(dx)

            elif a_key in num_coords and b_key in num_coords and (a_coord[0] + dx, a_coord[1]) not in num_coords.values():
                transitions[(a_key, b_key)] = y_arrow * abs(dy) + x_arrow * abs(dx)
            elif a_key in num_coords and b_key in num_coords and (a_coord[0], a_coord[1] + dy) not in num_coords.values():
                transitions[(a_key, b_key)] = x_arrow * abs(dx) + y_arrow * abs(dy)

            elif a_key in arrow_coords and b_key in arrow_coords and (a_coord[0] + dx, a_coord[1]) not in arrow_coords.values():
                transitions[(a_key, b_key)] = y_arrow * abs(dy) + x_arrow * abs(dx)
            elif a_key in arrow_coords and b_key in arrow_coords and (a_coord[0], a_coord[1] + dy) not in arrow_coords.values():
                transitions[(a_key, b_key)] = x_arrow * abs(dx) + y_arrow * abs(dy)

            elif arrow_priority.index(x_arrow) < arrow_priority.index(y_arrow):
                transitions[(a_key, b_key)] = x_arrow * abs(dx) + y_arrow * abs(dy)
            else:
                transitions[(a_key, b_key)] = y_arrow * abs(dy) + x_arrow * abs(dx)

populate_transitions(num_coords)
populate_transitions(arrow_coords)

def get_sequence(code):
    s = ""
    prev = "A"
    for c in code:
        s += transitions[(prev, c)] + "A"
        prev = c
    return s

def iterate_sequence(code, n):
    c = code
    for _ in range(n):
        c = get_sequence(c)
    return c

def get_complexity(code, n):
    s = iterate_sequence(code, n)
    num = int(code.lstrip("0").replace("A", ""))
    print(num, len(s))
    return num * len(s)
    
print(sum([get_complexity(code, 3) for code in lines]))