import re
from z3 import *

with open('input/13.txt', 'r') as f:
    input = f.read()

machines = [m.split("\n") for m in input.split('\n\n')]
for i, (a, b, prize) in enumerate(machines):
    ax, ay = re.search(r'Button A: X\+(\d+), Y\+(\d+)', a).groups()
    bx, by = re.search(r'Button B: X\+(\d+), Y\+(\d+)', b).groups()
    px, py = re.search(r'Prize: X=(\d+), Y=(\d+)', prize).groups()
    machines[i] = (int(ax), int(ay), int(bx), int(by), int(px), int(py))

def solve(machine, offset=0):
    ax, ay, bx, by, px, py = machine
    a = Int('a')
    b = Int('b')
    o = Optimize()
    o.add(a >= 0, b >= 0)
    o.add(a * ax + b * bx == px + offset)
    o.add(a * ay + b * by == py + offset)
    o.minimize(3 * a + b)
    if o.check() == sat:
        return o.model().eval(3 * a + b).as_long()
    return 0

part_1 = 0
part_2 = 0
for machine in machines:
    part_1 += solve(machine)
    part_2 += solve(machine, 10000000000000)

print("Part 1:", part_1)
print("Part 2:", part_2)
    