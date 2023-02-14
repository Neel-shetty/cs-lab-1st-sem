import random
import string

def gen_password(length):
    password=''
    for i in range(length):
        password = password + random.choice(string.ascii_letters+string.digits+string.punctuation)
    return password

length = int(input('Enter the length of the password (8-16) - '))
for i in range(5):
  print(gen_password(length if (length>=8 and length<=16) else 10))




