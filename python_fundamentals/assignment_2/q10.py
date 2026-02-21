guess_no = 46

number = int(input("enter the number : "))

if number == guess_no:
    print("Correct!")

elif number < guess_no:
    print("Too low")

else:
    print("Too high")



