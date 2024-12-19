with open('input/19.txt', 'r') as f:
    sequences, patterns = f.read().split("\n\n")

sequences = set(sequences.split(", "))
patterns = patterns.split("\n")

def count_ways_to_construct(s: str, parts: set[str]) -> int:
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in parts:
                dp[i] += dp[j]
    return dp[n]
    
ways_to_construct = [count_ways_to_construct(pattern, sequences) for pattern in patterns]    

print("Part 1:", sum(1 for ways in ways_to_construct if ways > 0))
print("Part 2:", sum(ways_to_construct))