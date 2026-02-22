tup = (1,2,3,4,5,6)

tup_even = tuple(n for n in tup if n % 2 == 0)
tup_odd = tuple(n for n in tup if n % 2 != 0)


print(tup_even)
print(tup_odd)