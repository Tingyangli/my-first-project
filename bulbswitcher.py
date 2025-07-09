n = int(input())

state = 0
for bulb in range (n+1):
    switch = 0
    for i in range(1,bulb+1):
        if bulb%i == 0:
            switch += 1
    if switch %2 != 0:
        state +=1
print(state)
                