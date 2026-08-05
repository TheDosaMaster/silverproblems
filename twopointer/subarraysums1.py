n,x = map(int,input().split())
a = list(map(int,input().split()))
count = 0
prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + a[i])

r = -1
for l in range(n):
    while r < n and prefix[r+1] - prefix[l] < x:
        r += 1
    if r < n and prefix[r+1] - prefix[l] == x:
        count += 1
print(count)