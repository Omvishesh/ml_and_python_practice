def all_even(a,b):
    for n in range (a, b+1):
        if n % 2 == 0:
            print(n)
        n += 1

all_even(2,10)