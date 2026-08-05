n = int(input())
arr = list(map(int,input().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + arr[i])

freq = [0] * n
count = 0
for val in prefix:
    rem = val % n
    count += freq[rem]
    freq[rem] += 1

print(count)