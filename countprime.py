import time
n = int(input())
start = time.time()

primes = [2]
for i in range(2,n+1,2):
    for prime in primes: 
        if i % prime == 0:
            break
    else:
        primes.append(i)
    # print(primes)
        
    
print (len(primes))

end = time.time()
duration = end - start 

print(duration)
