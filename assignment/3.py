import random
import string
import re

def generate_password( pattern):
    password = ""
    for i in range(len(pattern)):
        #using regex to match string character to a pattern
        if re.findall("[A-Z]",pattern[i]):
            password += random.choice(string.ascii_uppercase)
        elif re.findall("[a-z]",pattern[i]):
            password += random.choice(string.ascii_lowercase)
        elif re.findall('[0-9]',pattern[i]):
            password += random.choice(string.digits)
        elif re.findall("[!-~]",pattern[i]):
            password += random.choice(string.punctuation)
    return password

# accept input pattern from user
pattern = input("Enter password pattern (Ex: Aa5*D): ")

# generate 5 different passwords
for i in range(5):
    password = generate_password(pattern)
    print(password)

    