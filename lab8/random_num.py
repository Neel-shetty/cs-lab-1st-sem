#program to generate random numbers and store it in a file
import random

idk = open('test.txt','w')
# print(idk.readline())
for i in range(20):
  print(idk.write(str(random.randint(0,100))+'\n'))