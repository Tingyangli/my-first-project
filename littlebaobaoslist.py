littlebaobaoslist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,97]
#list [start:stop:step]
print (littlebaobaoslist[0::])

#this finds the position of the number in the list and print it
for number in (littlebaobaoslist):
    print(littlebaobaoslist[number:number+1])

#enumerate()means it goes number by number 
x=1
for i, number in enumerate(littlebaobaoslist):
    print (littlebaobaoslist[i:i+x])
    i+=x
    x+=1

#'*'in front of 
cutelist = [*'love'*5,*'baobao'*5]
print (cutelist)

lovelist = ['i','love','you','too','baobao'*500]
print (lovelist[0]+' '+lovelist[1]*500 + lovelist[4])
print (len(lovelist))