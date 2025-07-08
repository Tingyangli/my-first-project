n = int(input())
#def happy(n):


# for digit in str(n):
#     print (int(digit))
digitslist = []
while True:
    digits = [int(d) for d in str(n)]
    digitsprocess = 0

    for digit in digits:
        digitsprocess += digit**2
    n = digitsprocess
    
        
    if n == 1:
        print("true")
        print (digitslist)
        break 
    if n in digitslist:
        print("False")
        print (digitslist)
        break

    digitslist.append(n)
        
    print (digitslist)
