user = input("enter the number : ")

while user:
    if user == "Quit":
        break
    elif int(user) >= 0:
        print("positive")
    elif int(user) < 0:
        print('negative')