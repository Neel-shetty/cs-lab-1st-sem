#program to find duplicate character in a str and store in a list
str = input('Enter a string - ')
str_list = list(str)
idk = []
for i in str:
  str_list.remove(i)
  count = 0
  if i in idk:
    count +=1
    dic = {i:count}
  elif i in str_list:
    idk.append(i)



print(idk)