n = int(input())

def fibonacci(n):
    baobaofibs=[0,1]
    a=0
    i=len(baobaofibs)
    while a<n:
        new = baobaofibs[i-1]+baobaofibs[i-2]
        baobaofibs.append(new)
        a+=1
        i=len(baobaofibs)
    print(baobaofibs[i-1])
fibonacci(n)