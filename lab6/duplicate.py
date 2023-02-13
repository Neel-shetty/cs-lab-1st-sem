#program to find duplicate character in a str and store in a list
str = input('Enter a string - ')
str_list = list(str)
res = []
for i in str:
  str_list.remove(i)
  count = 0
  if i in res:
    continue
  elif i in str_list:
    res.append(i)

print(res)



str = input('Enter a string - ')
char_count = {}
for char in str:
  if char in char_count:
    char_count[char] += 1
  else:
    char_count[char] = 1

print(char_count)


