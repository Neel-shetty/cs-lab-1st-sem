#ap sequence 
#This program is not for lab manual
start_num = int(input('enter the first number - '))
diff = int(input('enter the diff - '))
num_of_terms = int(input('enter the number of terms - '))

for i in range(num_of_terms):
  ap = start_num + (i)*diff
  print(ap)
