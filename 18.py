with open('input/18.txt', 'r') as f:
    lines = f.read().splitlines()

fallen_bytes = set()
for i in range(1024):
    x,y = lines[i].split(",")
    fallen_bytes.add((int(x) + int(y) * 1j))

start = 0
end = 70 + 70j

def shortest_path_to_end(start, end, fallen_bytes):
    queue = [(start, 0)]
    visited = set()
    while queue:
        pos, steps = queue.pop(0)
        if pos == end:
            return steps
        if pos in visited:
            continue
        visited.add(pos)
        for move in [1, -1, 1j, -1j]:
            new_pos = pos + move
            if new_pos in fallen_bytes:
                continue
            if new_pos.real < 0 or new_pos.imag < 0:
                continue
            if new_pos.real > end.real or new_pos.imag > end.imag:
                continue
            queue.append((new_pos, steps + 1))
    return -1

print("Part 1:", shortest_path_to_end(start, end, fallen_bytes))

for i in range(1024, len(lines)):
    x,y = lines[i].split(",")
    fallen_bytes.add((int(x) + int(y) * 1j))
    if shortest_path_to_end(start, end, fallen_bytes) == -1:
        print("Part 2:", lines[i])
        break