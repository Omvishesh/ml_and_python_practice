list1 = [1,2,3]
list2 = [3,4]

set_1 = set()

set_2 = set()

for n in list1:
    set_1.add(n)

for i in list2:
    set_2.add(i)
    
new_set = set_1.intersection(set_2)
print(new_set)

if new_set == set():
    print("no common element found")

else:
    print("common elements found")

