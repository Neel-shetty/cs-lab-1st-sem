#check if a number is a perfect number or not (1+2+3=6, 6 is a perfect number here)
# interval = int(input("enter a range - "))
range_start = int(input("enter the starting value of the range - "))
range_end = int(input("enter the ending value of the range - "))
for i in range(range_start,range_end):
  num = i
  sum = 0 

  for i in range(1,num):
    if(num%i==0):
      sum = sum + i

  if sum == num:
    print('{} is a perfect number'.format(num))