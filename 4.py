with open('input/4.txt', 'r') as f:
    text = f.read().splitlines()


width = len(text[0])
height = len(text)

matches = 0

def check_match(i, j, dx, dy):
    indices = [(i + dx * k, j + dy * k) for k in range(4)]
    for i, j in indices:
        if i < 0 or i >= height or j < 0 or j >= width:
            return False
    t = [text[i][j] for i, j in indices]
    if "".join(t) == "XMAS":
        return True
    return False

directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (-1, 0)]

for i in range(height):
    for j in range(width):
        for dx, dy in directions:
            if check_match(i, j, dx, dy):
                matches += 1

print("Part 1:", matches)

def is_cross_mas(i, j):
    if text[i][j] != "A":
        return False
    if i + 1 >= height or j + 1 >= width:
        return False
    if i - 1 < 0 or j - 1 < 0:
        return False
    diag1 = text[i + 1][j + 1] + text[i - 1][j - 1]
    diag2 = text[i + 1][j - 1] + text[i - 1][j + 1]
    return "".join(sorted(diag1)) == "MS" and "".join(sorted(diag2)) == "MS"

count = 0
    
for i in range(height):
    for j in range(width):
        if is_cross_mas(i, j):
            count += 1

print("Part 2:", count)