import time
import math
n = int(input())
start = time.time()

primelist = [True]*n
for x in range(len(primelist)):
    primelist[x] = False
    if x > 0:
        break

print(primelist)
for a in range(len(primelist)):
    if primelist[a] == True:
        for i in range(a,n): #int(n**0.5)+2):
            if i*a >= len(primelist):
                break
            primelist[i*a] = False
       
    
print (sum(primelist))
print(primelist)

end = time.time()
duration = end - start 

print(duration)