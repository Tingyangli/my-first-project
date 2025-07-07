import math
# result = math.comb(5, 2)
# print(result)
#stairs = math.comb (n,i) +...+ math.comb (n-i, i)

n= int(input())
stairs = 0
for i in range (n):
    stairs += math.comb (n,i)
    n -= 1
    if n % 2 == 0:
        if i == n:
            break
    else:
        if i == n+1:
            break
        
print (stairs)