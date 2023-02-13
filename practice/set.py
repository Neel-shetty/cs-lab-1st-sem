#set ope, include union diff, superset, subset
set1 = set()
set2 = set()
# courses = {'test,', "abc", "xyz"}
# cour= {'test,', "ffgh", "yui"}
# courses.update(cour)
# print(courses)
# for i in courses:
#     print(i)
# set3 = {1,2,3,4,5,67,89,0}

# num = input('enter a number - ')
# nums = num.split(' ')
# idk = set())
# for i in nums:
#   idk.add(int(i))
# print(idk,"set")
for i in range(20):
  set1.add(i)
  set2.add(i+(i*2))
# print(len(set1),len(set2))

a = {3,4,9}
b = {5,4,10}
c = a.union(b) - a.intersection(b) # symmertic diff
print(c)
print((a|b)-(a&b))