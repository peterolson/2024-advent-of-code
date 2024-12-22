with open('input/22.txt', 'r') as f:
    lines = f.read().splitlines()

nums = [int(x) for x in lines]
    

def next(s):
    x = s * 64
    s ^= x
    s %= 16777216

    x = s // 32
    s ^= x
    s %= 16777216

    x = s * 2048
    s ^= x
    s %= 16777216

    return s

def nth(s, n):
    for _ in range(n):
        s = next(s)
    return s


print("Part 1:", sum(nth(x, 2000) for x in nums))

def get_prices(s, n):
    ps = []
    previous_price = s % 10
    for _ in range(n):
        s = next(s)
        p = s % 10
        change = p - previous_price
        ps.append((p, change))
        previous_price = p
    return ps

def get_sequences(s, n):
    ps = get_prices(s, n)
    sequences = {}
    for i in range(3, n):
        trailing_4 = ps[i-3:i+1]
        sequence = tuple(x[1] for x in trailing_4)
        if sequence in sequences:
            continue
        price = ps[i][0]
        sequences[sequence] = price
    return sequences

all_sequences = set()
sequence_prices = []
for x in nums:
    sequences = get_sequences(x, 2000)
    sequence_prices.append(sequences)
    for k, v in sequences.items():
        all_sequences.add(k)

best_price = 0
best_sequence = None
for s in all_sequences:
    total_price = sum(sp.get(s, 0) for sp in sequence_prices)
    if total_price > best_price:
        best_price = total_price
        best_sequence = s

print("Part 2:", best_price)