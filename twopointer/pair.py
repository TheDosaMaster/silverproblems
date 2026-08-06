import sys

sys.stdin = open('pairup.in', 'r')
sys.stdout = open('pairup.out', 'w')
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a = sorted(a, key=lambda x: x[1])
left = 0
right = n - 1
m = 0

while left < right:
    sum = a[left][1] + a[right][1]
    m = max(m, sum)
    if a[left][0] < a[right][0]:
        a[right][0] -= a[left][0]
        left +=1
    elif a[left][0] > a[right][0]:
        a[left][0] -= a[right][0]
        right -= 1
        
    else:
        left += 1
        right -= 1
print(m)