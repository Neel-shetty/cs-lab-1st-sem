import math

def check_discriminant(a,b,c):
  discriminant = (b**2) - (4 * a * c)
  print("the discriminant is - {}".format(discriminant))
  if discriminant == 0:
    print("roots are real and same")
  elif discriminant > 0:
    print("roots are real and different")
  elif discriminant < 0:
    print("roots are complex")
  x = (-b-math.sqrt((discriminant)))/(2*a)
  y = (-b+math.sqrt((discriminant)))/(2*a)
  print("The roots are {} and {}".format(x,y))

a=int(input('enter the first number - '))
b=int(input('enter the second number - '))
c=int(input('enter the third number - '))
check_discriminant(a,b,c)
