list = [1, 2, 3, 4, 2, 2]

seen = set()
duplicate = set()

for n in list:
    if n in seen: 
        duplicate.add(n)
    else:
        seen.add(n)

print(f"the elemets that appear more than once are {duplicate}")