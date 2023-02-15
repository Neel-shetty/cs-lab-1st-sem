import random

f = open('test.txt','w')
i = 0 
while i<10:
    number = random.randint(1,500)
    f.write(str(number)+'\n')
    i+=1
f.close()