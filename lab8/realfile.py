#write a program to display first n lines in a text file
idk = open('test.txt','w')
# print(idk.readline())
for i in range(20):
  print(idk.write(str(i)+'\n'))