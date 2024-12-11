with open('input/11.txt', 'r') as f:
    lines = f.read().splitlines()

initial_stones = list(map(int, lines[0].split()))
stone_dict = {s: initial_stones.count(s) for s in initial_stones}

def transform_stone(n):
    if n == 0:
        return [1]
    s = str(n)
    if len(s) % 2 == 0:
        half = len(s) // 2
        return [int(s[:half]), int(s[half:])]
    return [n * 2024]

def blink(stone_dict):
    new_stones = {}
    for s, count in stone_dict.items():
        transformed = transform_stone(s)
        for t in transformed:
            if t in new_stones:
                new_stones[t] += count
            else:
                new_stones[t] = count
    return new_stones

def count_stones(stone_dict):
    return sum(stone_dict.values())

s = stone_dict
for i in range(75):
    s = blink(s)
    if i + 1 == 25:
        print("Part 1:", count_stones(s))
    if i + 1 == 75:
        print("Part 2:", count_stones(s))