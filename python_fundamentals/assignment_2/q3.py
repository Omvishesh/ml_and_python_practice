def digits (a):
    while a != 0:
        one_less = a%10
        print(one_less)
        a = int(a/10)

digits(312)

# a = 312
# b = a%10
# print(b) #=> 2
# a = int(a / 10)
# print(a) #=> 31