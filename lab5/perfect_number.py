#check if a number is a perfect number or not (1+2+3=6, 6 is a perfect number here)
num = int(input("enter a number - "))
sum = 0 

for i in range(1,num):
  if(num%i==0):
    sum = sum + i

if sum == num:
  print('{} is a perfect number'.format(num))
else: 
  print('{} is not a perfect number'.format(num))