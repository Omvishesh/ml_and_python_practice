list1 = [1,2,7]
list2 = [2,4,5]

result = list1

for n in list2:
    result.append(n)
    result.sort()
    
print(result)