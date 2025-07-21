n = int(input())
m = int(input())

selfdividingnumbers=[]

for x in range (n,m+1):
    digits = [int(d) for d in str(x)]
    #print (digits)
    for digit in digits:
        if digit == 0:
            break
    
        
        if x % digit != 0:
            break
    else:
        selfdividingnumbers.append(x)

print(selfdividingnumbers)