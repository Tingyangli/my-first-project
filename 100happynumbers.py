
x = int(input("hello,have a happy day:) these are the happy numbers until"))
happylist = []
for n in range (x+1):

    start = n

    digitslist = []
    
    while True:
        digits = [int(d) for d in str(n)]
        digitsprocess = 0

        for digit in digits:
            digitsprocess += digit**2
        n = digitsprocess
        
            
        if n == 1:
            happylist.append(start)
            break 
        if n in digitslist:
            break

        digitslist.append(n)
            
print (happylist)

num = 0 
for i in happylist:
    num +=1
print ("there are",num,"of happy numbers in",x)

print(len(happylist))
