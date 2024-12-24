with open('input/24.txt', 'r') as f:
    values, expressions = f.read().split("\n\n")
    values = values.split("\n")
    values = [value.split(": ") for value in values]
    expressions = [expression.split(" -> ") for expression in expressions.split("\n")]
    expressions = {expression[1]: expression[0].split() for expression in expressions}

evaluated_values = {}
for name, bit in values:
    evaluated_values[name] = int(bit)

def evaluate(name):
    if name in evaluated_values:
        return evaluated_values[name]
    lhs, operator, rhs = expressions[name]
    lhs = evaluate(lhs)
    rhs = evaluate(rhs)
    if operator == 'AND':
        evaluated_values[name] = lhs & rhs
    elif operator == 'OR':
        evaluated_values[name] = lhs | rhs
    elif operator == 'XOR':
        evaluated_values[name] = lhs ^ rhs
    return evaluated_values[name]

for name in expressions:
    evaluate(name)

z_names = sorted([name for name in expressions if name.startswith('z')], reverse=True)
z_value = int("".join([str(evaluated_values[name]) for name in z_names]), 2)

print(z_value)

def test_bit(n):
    global evaluated_values
    evaluated_values = {}
    for i in range(len(z_names) - 1):
        suffix = ("0" + str(i))[-2:]
        x_name = f"x{suffix}"
        y_name = f"y{suffix}"
        if i == n:
            evaluated_values[x_name] = 0
            evaluated_values[y_name] = 1
        else:
            evaluated_values[x_name] = 0
            evaluated_values[y_name] = 0
    return evaluate("z" + ("0" + str(n))[-2:])

for i in range(len(z_names) - 1):
    t = test_bit(i)
    if t != 1:
        print(i, t)


# 7, 20, 28, 35


# bits = len(z_names) - 1

# new_expressions = {}
# for i in range(bits):
#     suffix = ("0" + str(i))[-2:]
#     next_suffix = ("0" + str(i + 1))[-2:]
#     if i == 0:
#         new_expressions[f"z{suffix}"] = [f"x{suffix}", "XOR", f"y{suffix}"]
#         new_expressions[f"c{next_suffix}"] = [f"x{suffix}", "AND", f"y{suffix}"]
#         continue
#     new_expressions[f"xor{suffix}"] = [f"x{suffix}", "XOR", f"y{suffix}"]
#     new_expressions[f"z{suffix}"] = [f"xor{suffix}", "XOR", f"c{suffix}"]
#     new_expressions[f"and{suffix}"] = [f"x{suffix}", "AND", f"y{suffix}"]
#     new_expressions[f"cand{suffix}"] = [f"xor{suffix}", "AND", f"c{suffix}"]
#     if i < bits - 1:
#         new_expressions[f"c{next_suffix}"] = [f"and{suffix}", "OR", f"cand{suffix}"]
#     else:
#         new_expressions[f"z{next_suffix}"] = [f"and{suffix}", "OR", f"cand{suffix}"]

# with open('input/24_adder.txt', 'w') as f:
#     for name, expression in new_expressions.items():
#         f.write(f"{expression[0]} {expression[1]} {expression[2]} -> {name}\n")

# swaps = [["tqr", "hth"]]
# with open('input/24_adder_input.txt', 'w') as f:
#     renames = {}
#     for old, new in swaps:
#         renames[old] = new
#         renames[new] = old
#     for name, expression in expressions.items():
#         f.write(f"{expression[0]} {expression[1]} {expression[2]} -> {renames.get(name, name)}\n")

# replacements = {}
# def do_transfer():
#     with open('input/24_adder.txt', 'r') as f:
#         adder_expressions = f.read()
#     with open('input/24_adder_input.txt', 'r') as f:
#         adder_input = f.read()

#     for line in adder_expressions.splitlines():
#         if "\t" in line:
#             continue
#         expression, name = line.split(" -> ")
#         lhs, operator, rhs = expression.split()

#         for input_line in adder_input.splitlines():
#             input_expression, input_name = input_line.split(" -> ")
#             input_lhs, input_operator, input_rhs = input_expression.split()

#             if ((lhs == input_lhs and rhs == input_rhs) or (lhs == input_rhs and rhs == input_lhs)) and operator == input_operator:
#                 adder_input = adder_input.replace(input_line + "\n", "")
#                 adder_expressions = adder_expressions.replace(line + "\n", line + "\t" + input_line + "\n")
#                 adder_input = adder_input.replace(input_name, name)
#                 if input_name in replacements:
#                     print("Already replaced", input_name, replacements[input_name], name)
#                 replacements[input_name] = name
#                 with open('input/24_adder_input.txt', 'w') as f:
#                     f.write(adder_input)
#                 with open('input/24_adder.txt', 'w') as f:
#                     f.write(adder_expressions)
#                 return True

# for i in range(223):
#     print(i)
#     if do_transfer():
#         print("Transfered")
# print(replacements)