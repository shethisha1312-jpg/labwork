# 1) 
#Create a class person with attributes such as name and age
#- write a method to display the details
#-create multiple objects and call the method for each

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def display(self):
#         print("Name is:",self.name)
#         print("Age is:",self.age)
        
# p1 = Person("Isha",21)
# p2 = Person("Charmi",25)
# p3 = Person("Hetvi",22)

# p1.display()
# p2.display()
# p3.display()


# 2)

# Develop a class counter with an attribute count initialized to zero
#- Create method in increment the count and display the value using self

# class Counter:
#     def __init__(self):
#         self.count = 0
    
#     def increment(self):
#         self.count += 1
        
#     def display(self):
#         print("Count:",self.count)
        
# c = Counter()

# c.increment()
# c.increment()
# c.increment()

# c.display()

# 3) Explain the behavior when self is omitted in a method definition using a small example

# class Student:
#     def display():
#         print("Hello student")

# s = Student()
# s.display()

# 4) Write a program to create a class Book with private attributes title and author 
#- Add public methods to set and get these attributes

# class Book:
#     def __init__(self,title,author):
#         self.__title  = title
#         self.__author = author
        
#     def set_title(self,title):
#         self.__title = title
#     def set_author(self,author):
#         self.__author = author
        
#     def get_title(self):
#         return self.__title
    
#     def get_author(self):
#         return self.__author
    
# book = Book("Python Programming ","John smith")

# print("Title:",book.get_title())
# print("Author:",book.get_author())

# book.set_title("Advance Python")
# book.set_author("James")

# print("\n After updating:")
# print("Title:",book.get_title())
# print("Author:",book.get_author())


#5) Implement a class Account with a private attribute balanace
#- Create methods to deposit and withdraw money
#- Add a method to display the balance
#- Ensure balanace connot be accessed diractly

# class Account:
#     def __init__(self,balance):
#         self.__balance = balance
#     def deposit(self , amount):
#         self.__balance += amount
#         print("Amount deposited",amount)
        
        
#     def withdraw(self , amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print("Amount Withdraw:",amount)
#         else:
#             print("Insuffcient balance")
#     def display_balance(self):
#         print("Balance:",self.__balance)
        
# account = Account(5000)
# account.display_balance()


# account.deposit(2000)
# account.display_balance()

# account.withdraw(1000)
# account.display_balance()


# 6) 
# Develop a program that users greeter and setter methods to validate the age 
#of a person ( e.g., age must be greater than 0).

# class Person:
#     def __init__(self,age):
#         self.__age =0
#         self.set_age(age)
        
#     def set_age(self , age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Invaid Age")
    
#     def get_age(self):
#         return self.__age

# p = Person(21)

# print("Age:",p.get_age())

# p.set_age(25)
# print("Updated Age:",p.get_age())

# p.set_age(-5)

# 7) 
# Create a class student with private attributes for name and marks(of three subjects)
# - Add a method to calculate and display the avrage
# -Add public method to calculate and display the gread based on marks

class Student:
    def __init__(self,name,m1,m2,m3):
        self.__name = name 
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
    
    def calculate_average(self):
        average = (self.__m1 + self.__m2 + self.__m3) / 3
        return average
    
    def display_average(self):
        average = self.calculate_average()
        print("Average:",average)
        
        
    def display_gread(self):
        average = self.calculate_average()
        print("Average:",average)
        
    def display_gread(self):
        average = self.calculate_average()
        
        if average >= 90:
            gread = "A+"
        elif average >= 80:
            gread = "A"
        elif average >= 70:
            gread = "B"
        elif average >= 60:
            gread = "c"
        elif average >= 50:
            gread = "D"
        else:
            gread = "F"
        
        print("Gread:",gread)
student = Student("Isha",85,90,80)
print("Name:",student._Student__name)

student.display_average()
student.display_gread()