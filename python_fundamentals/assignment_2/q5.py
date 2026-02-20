def digits (a):
    sum = 0
    while a != 0:
        one_less = a%10
        sum += one_less
        a = int(a/10)
    return sum

total = digits(312)
print(f" sum of all the digits are : {total}")