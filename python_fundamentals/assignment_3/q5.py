student_data = {
    "om": 90
}



while True:
    user_input = input("""enter one of the following for the desired operation :
                   A - Add a Student 
                   B - Update Marks
                   C - Search for a student
                   D - Display all students and marks
                   or quit to exit
                   Answer : 
                   """)
    if user_input == 'A':
        name = input("enter student name: ")
        marks = input("enter student marks: ")
        new_item = {name: marks}
        student_data.update(new_item)

    elif user_input == 'B':
        name = input("enter student name whose marks needs to be updated: ")
        marks = input("enter student marks: ")
        
        student_data[name]=marks
        print("marks has been updated")
        
    elif user_input == 'C':
        name = input("enter student name: ")
        
        print(f"the marks of {name} is {student_data.get(name)}")
        
    elif user_input =='D':
        print(f"{student_data.items()}")
        
    else:
        print("invalid input")