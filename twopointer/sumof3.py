n,x = map(int,input().split())
a = list(map(int,input().split()))
na = []
for i in range(n):
    na.append((a[i], i))
na.sort()

for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        total = na[i][0] + na[left][0] + na[right][0]

        if total == x:
            arr = sorted([na[i][1] + 1, na[left][1] + 1, na[right][1] + 1])
            print(arr[0], arr[1], arr[2])
            exit()
        elif total < x:
            left += 1
        else:
            right -= 1

print("IMPOSSIBLE")
