salary = int(input("enter the salary : "))

if salary < 30000:
    tax = (5 * salary) / 100
    print(f"your final tax rate is {tax}")
    
if salary > 30000 and salary < 70000 :
    tax = (5 * salary) / 100
    print(f"your final tax rate is {tax}")

if salary > 70000:
    tax = (5 * salary) / 100
    print(f"your final tax rate is {tax}")
