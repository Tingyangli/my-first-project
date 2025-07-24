from collections import Counter
n = list(map(int, input().split()))
unique = set(n)
number = 0 
for i in unique: 
    if i == 0:
        number += 1 
        continue
    if n.count(i) <= i+1:
        number += i+1
    if n.count(i) > i+1:

        if n.count(i) % (i+1) == 0:
            number += ((n.count(i)//(i+1))*(i+1))
        else:
            number += ((n.count(i)//(i+1)+1)*(i+1))

print(number)
print (Counter(n))


