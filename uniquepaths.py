import math

n = int(input())
m = int(input())

uniquepath = math.comb(m+n-2, n-1)
print (uniquepath)