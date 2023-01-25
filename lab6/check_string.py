#program to check if each character in a give string is an alphabet or a digit
import string
str = input("enter the string - ")

for i in str:
  if i in string.ascii_letters:
    print("{} is an alphabet".format(i))
  if i in string.digits:
    print("{} is a digit".format(i))
  if i in string.punctuation:
    print("{} is a symbol".format(i))

