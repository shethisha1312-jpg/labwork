# Write a Program to find the length of a 1D array without using any built-in function.
# For example,
# Input:
# Enter array size: 5
# Enter array elements:
# a[0] = 3
# a[1] = 7
# a[2] = 1
# a[3] = 8
# a[4] = 6

# Output:
# Length of an Array: 5

# n = int(input("Enter array size: "))
# array =[]

# for i in range(n):
#     element = int(input(f"a[{i}] = "))
#     array.append(element)
# count = 0
# for i in array:
#     count += 1
    
# print("Length of an array:",count)

#===================================================================================================

# Write a Program to find the average of a 1D array without using any built-in function.
# For example,
# Input:
# Enter array size: 5
# Enter array elements:
# a[0] = 12
# a[1] = 42
# a[2] = 18
# a[3] = 50
# a[4] = 26

# Output:
# Average of an Array: 29.6

# def avg(array):
#     total =0
#     count =0
    
#     for element in array:
#         total = total + element
#         count = count + 1
#     average = total/count
#     return average

# n = int(input("Enter array size: "))
# array =[]

# print("Enter array element :")
# for i in range(n):
#     element = int(input(f"a[{i}]:"))
#     array.append(element)

# average = avg(array)

# print("Average of array :",average)

# Write a Program to perform the addition operation of two 1D arrays & store it in another array. Keep in mind that both array sizes must be the same.
# For example,
# Input:
# Enter array size: 5

# arr1 = int(input("Enter array 1 size :"))
# arr2 = int(input("Enter array 2 size :"))

# if arr1 == arr2:
#     a = []
#     b = []
#     c = []

#     print("Enter element of 1st array :")
#     for i in range(arr1):
#         element = int(input(f"a[{i}]:"))
#         a.append(element)
#     print("Enter element of 2nd array :")
#     for i in range(arr2):
#         element = int(input(f"b{i}]:"))
#         b.append(element)
#     for i in range(arr1):
#         c.append(a[i]+b[i])
#     print("Addition of 2 array:",c)
# else:
#     print("Array size is  not bee same")
    
# 4) Create an array of numbers from 1 to 10.
#    Multiply each element by 2 and print the result

# first method
# array = [i for i in range(1, 11)]
# result = [x * 2 for x in array]
# print("Original array:", array)
# print("Result after multiplying each element by 2:", result)


# Second method 

# array = []
# array2 = []
# for i in range(1, 11):
#     array.append(i)
# for i in range(10):
#     array2.append(array[i] * 2)
# print("Original array:", array)
# print("Result after multiplying each element by 2:", array2)

# 5) Take user input for a number.
# Check if it exists in the array.
# Print the index if found, else print "Not Found".

# a = [1,78,5,43,90,7]

# print("Array:", a)
# num = int(input("Enter a number :"))

# for i in range(len(a)):
#     if a[i] == num:
#         print("Number found at index:", i)
    
#         break
#     else:
#         print("Not Found")


# 6) In a user-defined array (by taking input):
# Print all even numbers from the array.
# Print all odd numbers from the array.

# n = int(input("Enter array of size :"))
# a = []
# for i in range(n):
#     element = int(input(f"a[{i}] = "))
#     a.append(element)

# print("Array:", a)

# even_numbers = []
# odd_numbers = []

# for num in a:
#     if num % 2 == 0:
#         even_numbers.append(num)
#     else:
#         odd_numbers.append(num)

# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)4

# 7) In a 1D Array:
#    Print the first five elements.
#    Print every alternate element from the array.

# 8) Print the first, last, and middle elements of the array

# array = [10, 20, 30, 40, 50, 60, 70]

# n=0
# for element in  array:
#     n = n + 1
# print("First element:", array[0])
# print("Last element:", array[n-1])
# middle_index = n // 2
# print("Middle element:", array[middle_index])





