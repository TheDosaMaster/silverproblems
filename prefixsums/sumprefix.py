from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))
freq = defaultdict(int)
freq[0] = 1
count = 0
curr = 0

for val in a:
    curr += val
    count += freq[curr - x]
    freq[curr] += 1

print(count)

