from functools import cmp_to_key

with open('input/5.txt', 'r') as f:
    text = f.read()

rules, updates = text.split('\n\n')
rules = rules.split('\n')
updates = updates.split('\n')
updates = [update.split(',') for update in updates]

rules_dict = {}
for rule in rules:
    left, right = rule.split('|')
    if left in rules_dict:
        rules_dict[left].append(right)
    else:
        rules_dict[left] = [right]

def follows_rules(update):
    for i in range(len(update)):
        if update[i] not in rules_dict:
            continue
        disallowed_precedents = rules_dict[update[i]]
        precedents = update[:i]
        if any(precedent in disallowed_precedents for precedent in precedents):
            return False
    return True

def get_middle_item(list):
    return list[len(list) // 2]


sum = 0
for update in updates:
    if follows_rules(update):
        middle_item = get_middle_item(update)
        sum += int(middle_item)

print("Part 1:", sum)

def correct_update(update):
    return sorted(update, key=cmp_to_key(lambda x, y: -1 if x in rules_dict and y in rules_dict[x] else 1 if y in rules_dict and x in rules_dict[y] else 0))

sum = 0
for i in range(len(updates)):
    if not follows_rules(updates[i]):
        updates[i] = correct_update(updates[i])
        middle_item = get_middle_item(updates[i])
        sum += int(middle_item)

print("Part 2:", sum)