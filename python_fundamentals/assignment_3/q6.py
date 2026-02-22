words = ["apple", "banana", "kiwi", "cherry", "mango"]

data = {}

for i in words:
    length = len(i)
    new_item = {i : length}
    print(new_item)
    data.update(new_item)
    
    
print(data)