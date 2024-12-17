with open('input/17.txt', 'r') as f:
    lines = f.read().splitlines()

register_a = int(lines[0].split()[-1])
register_b = int(lines[1].split()[-1])
register_c = int(lines[2].split()[-1])

program = list(map(int, lines[4].split()[1].split(',')))

program_pointer = 0
program_output = []

def combo_operand(operand: int):
    if operand <= 3:
        return operand
    if operand == 4:
        return register_a
    if operand == 5:
        return register_b
    if operand == 6:
        return register_c
    raise ValueError(f'Invalid combo operand {operand}')

def adv(operand: int):
    global register_a
    res = register_a // (2 ** combo_operand(operand))
    register_a = res

def bxl(operand: int):
    global register_b
    register_b = register_b ^ operand

def bst(operand: int):
    global register_b
    register_b = combo_operand(operand) % 8

def jnz(operand: int):
    global program_pointer
    if register_a != 0:
        program_pointer = operand - 2

def bxc(operand: int):
    global register_b
    register_b = register_b ^ register_c

def out(operand: int):
    program_output.append(combo_operand(operand) % 8)

def bdv(operand: int):
    global register_b
    res = register_a // (2 ** combo_operand(operand))
    register_b = res

def cdv(operand: int):
    global register_c
    res = register_a // (2 ** combo_operand(operand))
    register_c = res

operations = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

while 0 <= program_pointer < len(program):
    operation = program[program_pointer]
    operand = program[program_pointer + 1]
    operations[operation](operand)
    program_pointer += 2

print("Part 1:", ",".join(map(str,program_output)))

# 2,4,1,3,7,5,4,2,0,3,1,5,5,5,3,0

# WHILE A != 0:
    # bst 4: B = A % 8
    # bxl 3: B = B ^ 3
    # csv 5: C = A // 2 ** B
    # bxc: B = B ^ C
    # adv 3: A = A // 8
    # bxl 5: B = B ^ 5
    # out 5: B % 8

target_output = "".join(map(str, program))

def run(a: int):
    b = 0
    c = 0
    output = []
    while a != 0:
        b = a % 8
        b = b ^ 3
        c = a // (2 ** b)
        b = b ^ c
        a = a // 8
        b = b ^ 5
        output.append(b % 8)
    return "".join(map(str, output))

encountered_prefixes = set()
prefix_queue = [""]
length = len(target_output)
lowest_match = None
while len(prefix_queue) > 0:
    prefix = prefix_queue.pop(0)
    if prefix in encountered_prefixes:
        continue
    encountered_prefixes.add(prefix)
    #print(prefix, len(matches))
    for i in range(8):
        s = prefix + str(i) + "0" * (length - len(prefix) - 1)
        a = int(s, 8)
        result = run(a)
        if len(result) < length:
            continue
        if result == target_output:
            if lowest_match is None or a < lowest_match:
                lowest_match = a
                print("Part 2:", lowest_match)
                exit()
        idx = length - len(prefix) - 1
        if target_output[idx] == result[idx]:
            prefix_queue.append(prefix + str(i))