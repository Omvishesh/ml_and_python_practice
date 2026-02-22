user_input = input("Enter a string: ")

set_string = set()
counter = 0
for n in user_input:
    set_string.add(n)
    
for n in set_string:
    counter += 1
   
print(f"all unique characters are : {set_string}")
print(f"count of characters are : {counter}")