t = int(input())

for q in range(t):
    n = int(input())
    s =str(input())
    evens = [0] *26
    odds = [0] *26
    if n % 2 == 0:
        for i in range(n):
            index = ord(s[i])-97
            if i % 2 == 0:
                odds[index] +=1
            else:
                evens[index] +=1
        evenchange = n/2-max(evens)
        oddchange = n/2 - max(odds)

        print(int(oddchange+evenchange))
    else:
        preodd = [0] *26
        preeven = [0] * 26
        even = [0] *26
        odd = [0] *26
        ans = float('inf')
        for i in range(n):
            index = ord(s[i])-97
            if i % 2 == 1:
                odd[index] +=1
            else:
                even[index] +=1
        for rem in range(n):
            
            index = ord(s[rem])-97
            if rem % 2 == 1:
                odd[index] -=1
            else:
                even[index] -=1
            maxodd = 0
            maxeven = 0
            for j in range(26):
                count = preodd[j] +even[j]
                maxodd = max(count,maxodd)
            for j in range(26):
                count = preeven[j] +odd[j]
                maxeven = max(count,maxeven)
            ans = min(ans,n-maxodd-maxeven)
            if rem % 2 == 1:
                preodd[index] +=1
            else:
                preeven[index] +=1
        
        print(ans)
    
                
