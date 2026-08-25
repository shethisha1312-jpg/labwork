# 1) WAP that creates multiple objects of a class and delete them using the del keyword.
#-observe the behavior(using the destructor)

# class Student:
#     def __init__(self,name):
#         self.name = name
#         print(f"Object created for {self.name}")
        
#     def __del__(self):
#         print(f"Destructor called for {self.name}")
        
# s1 = Student("Isha")
# s2 = Student("Charmi")
# s3 = Student("hitu")

# print("All objects are created")

# del s1
# del s2
# del s3

# print("All object are deleted.")

# 2) Create a class Animal with a constructor that initializes tha name 
# attribute- Add a method to display the name of the animal

# class Animal:
#     def __init__(self,name):
#         self.name = name
        
#     def display_name(self):
#         print("Animal Name:",self.name)
        
# a1 = Animal("Cow")

# a1.display_name()

# 3) WAP to demonstarate  a parameterized constructor in the class Rectangle
# - Initialized the lenght and width using the constructor and caluculate 
# the area

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
        
#     def calculate_area(self):
#         area = self.length + self.width
#         print("Area of rectangle :",area)
        
# r1 = Rectangle(10,5)

# r1.calculate_area()

# 4) Create a class Employee with a defualt counstructor to initialize 
#attributes and a destrouctor to display a farewell messege when the 
# object is deleted 

# class Employee:
#     def __init__(self):
#         self.name = "Isha"
#         self.employee_id = 101
#         self.salary = 25000
        
#         print("Employee object created")
#         print("Name:",self.name)
#         print("Employee ID:",self.employee_id)
#         print("Salary:",self.salary)
        
#     def __del__(self):
#         print("Employee object deleted.")
#         print("GoodBye!  Employee has left the organization")
        
# e1 = Employee()

# del e1

# 5) Create a class student with appropriate attributes and mwthod , along 
# with a constructor

class Student:
    def __init__(self, name , roll_no , course):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        
    def display_ditails(self):
        print("Student Name:",self.name)
        print("Roll no:",self.roll_no)
        print("Course :",self.course)
        
    def study(self):
        print(self.name,"Is studing..")
        
s1 = Student("Isha",101,"AI/ML")

s1.display_ditails()
s1.study()
