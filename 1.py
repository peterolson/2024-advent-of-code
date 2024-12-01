with open('input/1.txt', 'r') as f:
    lines = f.read().splitlines()

split_lines = [line.split('   ') for line in lines]
lefts = [line[0] for line in split_lines]
rights = [line[1] for line in split_lines]

lefts_sorted = sorted(lefts)
rights_sorted = sorted(rights)

sum_distances = sum([abs(int(lefts_sorted[i]) - int(rights_sorted[i])) for i in range(len(lefts_sorted))])
print("Part 1:", sum_distances)

appearances = {}
for item in rights:
    if item in appearances:
        appearances[item] += 1
    else:
        appearances[item] = 1

total_appearances = 0
for item in lefts:
    total_appearances += int(item) * appearances.get(item, 0)

print("Part 2:", total_appearances)