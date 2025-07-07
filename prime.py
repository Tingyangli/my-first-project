#divide = /
#// 7//3 = 2
#n = int(input())%int(input())
#print(n)
n = int(input())
def prime (n):
    baobaoprime = []
    for i in range(2,n+1):
        for a in range(2,i):
            b = i%a
            if b == 0:
                break
        else:
            baobaoprime.append(i)
    print (baobaoprime)
prime(n)
            
        

