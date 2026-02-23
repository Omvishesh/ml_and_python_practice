class Student:
    def __init__ (self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks
        
    def get_details(self):
        print(f"the marks of {self.__name} whose roll number is {self.__roll_no} is {self.__marks}")
        
    def set_details(self,name, roll_no, marks):
        if (marks < 0 or marks > 100):
            print("the marks is invalid please try again")
        elif name == "":
            print("the name is invalid please try again")
        elif (roll_no < 1 or roll_no> 100):
            print("the roll number is invalid please try again")
        else:
            self.__name = name
            self.__roll_no = roll_no
            self.__marks = marks

stu1 = Student("om", 38, 90)
stu1.get_details()
stu1.set_details("saket", 50, 95)
stu1.get_details()
stu1.set_details("aryan", 102, 95)