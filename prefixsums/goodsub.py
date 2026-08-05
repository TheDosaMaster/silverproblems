t = int(input())
for l in range(t):
    n = int(input())
    a = str(input())
    arr = list(a)
    new = [int(x) for x in arr]
    pre = [0]
    count = 0
    for i in range(n):
        
        pre.append(pre[-1] + new[i]) 
    
    freq = [0] * (2 * n + 3)
    offset = n + 1
    freq[offset] = 1
    for i in range(1, n + 1):
        key = pre[i] - i + offset
        count += freq[key]
        freq[key] += 1
    print(count)
