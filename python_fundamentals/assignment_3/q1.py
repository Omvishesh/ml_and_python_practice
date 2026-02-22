user_input = list(input("enter the word: "))

reversed_list = []
for n in user_input:
    reversed_list.insert(0,n)


if user_input == reversed_list:
    print("the word is palindrome")
else:    print("the word is not palindrome")
    
