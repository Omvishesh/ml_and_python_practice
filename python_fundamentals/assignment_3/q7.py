user_input = input("Enter a sentences: ")
counter = 0
for n in user_input:
    if n == ' ':
        counter += 1
    else:
        continue

print(counter)