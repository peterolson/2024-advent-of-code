with open('input/7.txt', 'r') as f:
    lines = f.read().splitlines()

equations = []
for line in lines:
    result, calculation = line.split(': ')
    operands = [int(x) for x in calculation.split()]
    result = int(result)
    equations.append((result, operands))

def is_satisfiable(equation, operations):
    result, operands = equation
    base = len(operations)
    keys = list(operations.keys())
    possibilities = base ** (len(operands) - 1)

    for i in range(possibilities):
        potential_result = operands[0]
        for j in range(len(operands) - 1):
            digit = i // (base ** j) % base
            key = keys[digit]
            potential_result = operations[key](potential_result, operands[j + 1])
        if potential_result == result:
            return True
    return False

operations = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y
}

sum = sum([equation[0] for equation in equations if is_satisfiable(equation, operations)])

print("Part 1:", sum)

operations["|"] = lambda x, y: int(str(x) + str(y))

sum = 0
for i, equation in enumerate(equations):
    if i % 10 == 9:
        print(f"Processing {i + 1}/{len(equations)}...")
    if is_satisfiable(equation, operations):
        sum += equation[0]

print("Part 2:", sum)