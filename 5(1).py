# Q1) take a user first namd and last name as input . print them in the formate 

# firstname=input("Enter first name :")
# lastname=input("Enter last name :")

# print(f'Hello {lastname},{firstname}')

# Q2) 

# item = "apple"
# price = 5.50

# print(f'The price of {item} is {price} dollars ')

# Q3) 

# str = input("Enter staring :")

# revered = str[::-1]

# print("Reversed is :",revered)

# if str == revered:
#     print("It Is palindrome ")
# else:
#     print("It Is not plindrome")


# Q4) 

# str  = input("Enter any string :")

# print("Uppercase :",str.upper())
# print("Lowercase :",str.lower())
# print("Title :",str.title())

# Q5) 

# sentence = " Machine Learning and AI are treanding"
# b=sentence.split()
# b[3] = "Artifical Inteligentce"

# print(" ".join(b))

# Q6) split string into list

text = "apple,banana,grapes"

fruits = text.split(",")
print(fruits)

words=["Python", "is", "awesome"]

sentence =""

for word in words:
    sentence=sentence + word + " "

print(sentence)



# Q7) check if a string starts with "Hello"and ends with "World"
#     - remove all non-alphabetic charachter from "Data123#science !"
#     - reverce the string "python"

# 1. Check if string starts with "Hello" and ends with "World"

# text = input("Enter a string: ")

# if text.startswith("Hello") and text.endswith("World"):
#     print("String starts with Hello and ends with World")
# else:
#     print("Condition not satisfied")


# 2. Remove all non-alphabetic characters

# first way to solve this 
#============================
# text = "Data123#Science!"

# result = ""

# for ch in text:
#     if ch.isalpha():
#         result = result + ch

# print(result)

#====================================

# second way to solve this program 
#====================================
# str="Data123#Science!"
# strlest=(list(str))
# stralpha=""
# for i in strlest:
#     if(i.isalpha()):
#         stralpha+= i
    
# print(stralpha)



# 3. Reverse the string "Python"

# text = "Python"

# reverse = ""

# for ch in text:
#     reverse = ch + reverse

# print(reverse)
