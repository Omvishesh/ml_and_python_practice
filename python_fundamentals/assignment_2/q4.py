def digits (a):
    count = 0
    while a != 0:
        one_less = a%10
        count += 1
        a = int(a/10)
    return count 
number = digits(3456)
print(f"count of numbers = {number}")