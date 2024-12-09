with open('input/9.txt', 'r') as f:
    disk_map = f.read()

blocks = []

id = 0
for i, char in enumerate(disk_map):
    if i % 2 == 0:
        blocks.append((id, int(char)))
        id += 1
    else:
        blocks.append((None, int(char)))

blocks_copy = blocks.copy()

def shift_left(blocks):
    new_blocks = []
    for block in blocks:
        if block[0] is not None:
            new_blocks.append(block)
            continue

        none_count = block[1]
        while none_count > 0:
            id, count = blocks.pop()
            if id == None:
                continue
            if count <= none_count:
                none_count -= count
                new_blocks.append((id, count))
            else:
                new_blocks.append((id, none_count))
                blocks.append((id, count - none_count))
                none_count = 0
    return new_blocks

def compute_checksum(blocks):
    checksum = 0
    i = 0
    for block in blocks:
        id, count = block
        if id is None:
            i += count
            continue
        checksum += id * (2 * i + count - 1) * count / 2
        i += count
    return int(checksum)

print("Part 1:", compute_checksum(shift_left(blocks)))

def shift_left_full_blocks(blocks):
    new_blocks = []
    for i, block in enumerate(blocks):
        if block[0] is not None:
            new_blocks.append(block)
            blocks[i] = (None, block[1])
            continue
        
        none_count = block[1]
        for i in range(len(blocks) - 1, -1, -1):
            id, count = blocks[i]
            if id == None:
                continue
            if count <= none_count:
                none_count -= count
                new_blocks.append((id, count))
                blocks[i] = (None, count)
                

        if none_count > 0:
            new_blocks.append((None, none_count))
    return new_blocks

print("Part 2:", compute_checksum(shift_left_full_blocks(blocks_copy)))

