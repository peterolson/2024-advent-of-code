import re
with open('input/3.txt', 'r') as f:
    text = f.read()

# find matches of pattern mul(123,456)
matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', text)

sum = 0
for match in matches:
    l, r = map(int, match)
    sum += l * r
print(sum)

# split into parts delimited by "don't()"
parts = re.split(r"don't\(\)", text)
all_matches = []
for i, part in enumerate(parts):
    if i == 0:
        all_matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', part)
        continue
    idx = part.find("do()")
    if idx != -1:
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', part[idx:])
        all_matches += matches

sum = 0
for match in all_matches:
    l, r = map(int, match)
    sum += l * r
print(sum)