# 1. wap to ask the user to enter names of their 3 favourite movies and store them in a list

# list=[]

# for i in range(1,4):
#     movie=input("enter your 3 favourite movie names ")
#     list.append(movie)

# print(list)

# program2

# movies=[]

# movies.append(input("enter your 1st favourite movie :"))
# movies.append(input("enter your 2nd favourite movie :"))
# movies.append(input("enter your 3rd favourite movie :"))

# print(movies)

# 2. wap to check a list contains a palindrome of elements.

# list=[1,2,3,2,1]

# list1=list.copy()

# list1.reverse()

# if list==list1:
#     print("the list is a palindrome")
    
# else:
#     print("the list is not palindrome")

# 3. wap to count the number of students with grade A in the folloing tuple

# grade=("C","D","A","A","B","B","A",)

# print("Number of students with grade A : ",grade.count("A"))

#4. wap to store the above values in a list & sort them from A to D

grade=["C","D","A","A","B","B","A"]
print("original list ",grade)
grade.sort()
print("sorted list is : ",grade)
