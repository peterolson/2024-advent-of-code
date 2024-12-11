from collections import Counter

with open('input/11.txt', 'r') as f:
    stones = list(map(int, f.readline().split()))

stone_count = Counter(stones)

def transform_stone(n):
    s = str(n)
    if n == 0:
        yield 1
    elif len(s) % 2 == 0:
        half = len(s) // 2
        yield int(s[:half])
        yield int(s[half:])
    else:
        yield n * 2024

def blink(stone_count : Counter):
    new_stones = Counter()
    for s, count in stone_count.items():
        for t in transform_stone(s):
            new_stones[t] += count
    return new_stones

s = stone_count
for i in range(75):
    s = blink(s)
    if i + 1 == 25:
        print("Part 1:", s.total())
    if i + 1 == 75:
        print("Part 2:", s.total())