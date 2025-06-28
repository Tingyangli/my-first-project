print('moikka')

n = int(input())

#print(baobaofibs[i - 1])
#print(baobaofibs[i - 2])
#print(len(baobaofibs))


def fibonacci (n):
    baobaofibs = [0, 1]
    a = 0            
    while a < n:
        i = len(baobaofibs)
        #x= (x-1)+(x-2)
        new = baobaofibs[i - 1] + baobaofibs[i - 2]
        baobaofibs.append(new)
       
        a += 1
    i = len(baobaofibs)
    
    print (baobaofibs[i-1])