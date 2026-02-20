

while True:
    user = input("enter the number : ")
    if user == "Quit":
        break
    elif int(user) >= 0:
        print("positive")
    elif int(user) < 0:
        print('negative')