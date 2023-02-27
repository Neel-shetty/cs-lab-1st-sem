import random
f = open('test.txt','w')

def write():
  for count in range(100):
      num = random.randint(1,10)
      f.write(str(num)+'\n')

write()

