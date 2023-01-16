# write a program to accept an integer number and find sum of digits
num = int(input("enter a number with multiple digits - "))
arr = list(str(num))

sum = 0
for i in arr:
  sum = int(i) + sum

print(sum)
