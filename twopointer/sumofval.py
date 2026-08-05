

n, x = map(int, input().split())
arr = list(map(int, input().split()))
a = []
for i in range(n):
    a.append((arr[i], i))
a.sort()
left = 0
right = n-1

while left < right:
    sum = a[left][0] + a[right][0]
    
    if sum == x:
        print(a[left][1]+1, a[right][1]+1)
        break
    elif sum < x:
        left += 1
    else:
        right -= 1
    
if left >= right:
    print("IMPOSSIBLE")