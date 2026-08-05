import sys
sys.stdin = open("div7.in","r")
sys.stdout = open("div7.out","w")
n = int(input())
arr = list(int(input()) for _ in range(n))


final = [0]
for i in range(len(arr)):
    final.append(final[-1] + arr[i])

l = 0
r = len(final)-1

while (l < r):
    diff = final[r]-final[l]
    
    if diff % 7 == 0:
        print(r-l)
        break
    elif diff % 7 > 3.5:
        r -= 1
    elif diff % 7 < 3.5:
        l += 1


