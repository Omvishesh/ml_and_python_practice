operation = input("enter the operation you want to perform ( + , - , * , / ): ")

a = int(input("enter the first number :"))
b = int(input("enter the second number :"))

def calculator(a, b, operation):
    if operation == '+':
        return a+b
    elif operation == '-':
        return a-b
    elif operation == '*':
        return a*b
    elif operation == '/':
        return a/b
    else:
        return "invalid operation"
    
result = calculator(a, b, operation)
print(result)