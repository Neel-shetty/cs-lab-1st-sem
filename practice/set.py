
set1 = set()
set2 = set()

for i in range(10):
  set1.add(i)
  set2.add(i+(i*2))
print(set1,set2)

print(set1&set2)
print(set1^set2)