with open('input/25.txt', 'r') as f:
    schematics = f.read().split("\n\n")

locks = set()
keys = set()

max_height = len(schematics[0].split("\n")) - 2

for schematic in schematics:
    rows = schematic.split("\n")
    is_lock = "." not in rows[0]

    heights = tuple(len([row[i] for row in rows if row[i] == "#"]) - 1 for i in range(len(rows[0])))
    if is_lock:
        locks.add(heights)
    else:
        keys.add(heights)

def fits(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] > max_height:
            return False
    return True

fit_count = 0

for lock in locks:
    for key in keys:
        if fits(lock, key):
            fit_count += 1

print(fit_count)