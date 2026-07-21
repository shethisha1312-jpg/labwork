# 1) number is even or odd check 

# num = int(input("enter any number :"))

# if num % 2 == 0:
#     print("number is Even ")
# else:
#     print("Number is Odd")

# -----------------------------------------------------------------

# 2)  Categorize Age Groups Using Nested if-else

# age = int(input("Enter your age :"))

# if age >= 0:
#     if age <= 12:

#         print("Child")

#     else:
#         if age <= 19:

#             print("Teenager")

#         else:
#             if age <= 59:

#                 print("Adult")

#             else:

#                 print("Senior")
# else:

#     print("Invalid Age")

#----------------------------------------------------------------

# 3) find largest number among of three number 

# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))
# c = int(input("Enter 3rd number:"))

# if a >=  b and a >= c:
#     print("Largest number is:", a)

# elif b >= a and b >= c:
#     print("Largest number is:", b)

# else:
#     print("Largest number is:", c)

#------------------------------------------------------------------

# 4) a Number is Neutral, Positive, or Negative Using Ladder if Statement

no = int(input("Enter a number: "))

if no > 0:
    print("Positive Number")

elif no  < 0:
    print("Negative Number")

else:
    print("Neutral Number")

