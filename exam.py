#baobaos advanced coding exam:
#1. print the values and stop as soon as one is higher than 10
#2. print all values under 10
#3. how much do all values add up to?

values = [8,1,6,12,3,10,12,2,1,1,8,11,23,56,2,77,0,4,9]
for n in values: 
    if n < 10:
        print (n)

print (values)

#x  = sum (values)
print (sum(values))

for n in values:
    if n > 9:
        break
    print (n)

i = 0
while values [i]<9:
    print (values[i])
    i += 1