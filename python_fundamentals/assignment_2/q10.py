guess_no = 46

number = int(input("enter the number : "))
while True:
    if number == guess_no:
        print("Correct!")
        break
    elif number < guess_no:
        print("Too low")
        number = int(input("enter the number : "))

    else:
        print("Too high")
        number = int(input("enter the number : "))



