def check_number(n):
  if n<0:
    print('{} is negative'.format(num))
  elif n==0:
    print('The entered number is zero')
  else:
    print('{} is positive'.format(num))

num = int(input('Enter a number - '))
check_number(num)


