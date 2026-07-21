# Q1) using for loop to print 1 to 20 number print and using countinue statment 

# for i in range (1 , 21):
#     if i % 4 == 0:
#         continue
#     print(i)

# Q2) print numbers from 1 to 10 stop the loop using the break statement when the number is 7

# i = 1
# while i <= 10:
#     if i == 7:
#         break
#     print(i)
#     i += 1

# Q3) print only consonants

# word = "python"

# for ch in word:
#     if ch in "AEIOU":
#         continue
#     print(ch)

# Q4) multiplication tables using nested loops

# n = int(input("Enter N :"))

# for i in range ( 1 , n+1):
#     for j in range(1,11):
#         print(i,"x",j,"=",i*j)
#     print()


# Q5) write A PATTERN USING 
#1
#12
#123
#1234
#12345

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# Q6) pattern
#5
#54
#543
#5432
#54321

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print()


#Q7) pattern
#5
#45
#345
#2345
#12345

# for i in range(5,0,-1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()


# Q8) pattern

#12345
#2345
#345
#45
#5

# for i in range(1,6):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()