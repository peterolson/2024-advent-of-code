with open('input/2.txt', 'r') as f:
    lines = f.read().splitlines()

def is_decreasing(nums):
    for i in range(1, len(nums)):
        if nums[i] >= nums[i - 1]:
            return False
    return True

def is_increasing(nums):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False
    return True

def is_monotonic(nums):
    return is_decreasing(nums) or is_increasing(nums)

def is_safe_distance(nums):
    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) > 3:
            return False
    return True

def is_safe(nums):
    return is_safe_distance(nums) and is_monotonic(nums)

total_safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    if is_safe(nums):
        total_safe += 1

print("Part 1:", total_safe)

def is_safe_with_removal(nums):
    for i in range(len(nums)):
        variation = nums[:i] + nums[i + 1:]
        if is_safe(variation):
            return True
    return False

total_safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    if is_safe_with_removal(nums):
        total_safe += 1

print("Part 2:", total_safe)