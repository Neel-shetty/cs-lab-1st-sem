import os
print(os.getcwd()) 
file = open('test.txt','r')
lines = 0
for i in file:
    lines = lines + 1
print(lines)
