import sys
sys.stdin = open("bcount.in","r")
sys.stdout = open("bcount.out","w")
n,q = map(int,input().split())
breeds =  list(int(input()) for _ in range(n))
queries = [list(map(int,input().split())) for _ in range(q)]

prefix = [[0,0,0]]
for i in range(n):
    new = prefix[-1][:]
    new[breeds[i]-1] += 1
    prefix.append(new)

for i in range(q):
    a,b = queries[i]
    ans = [prefix[b][0]-prefix[a-1][0],prefix[b][1]-prefix[a-1][1],prefix[b][2]-prefix[a-1][2]]
    print(ans[0],ans[1],ans[2])

    