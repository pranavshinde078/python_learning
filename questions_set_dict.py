#1. wap to store the following word meanings in the dict 
# "cat":"a samll animal",
# "table":["a piece of furniture","list of facts and figures"]

# dict={
#     "cat":"a samll animal",
#     "table":["a piece of furniture","list of facts and figures"]
# }
# print(dict)

#2. you are given a list of subjects for students. assume one classroom is required for 1 subject.how many classrooms are needed by all students.
# "python","java","c++","js","c","python","java","python","java","c++","c"
# set={"python","java","c++","js","c","python","java","python","java","c++","c"}
# print(set)
# print("total classrooms needed: ",len(set))


# 3. wap to enter marks of three subjects from the user and store them in a dict.start with an empty dict &add one by one.use subject name aas a key & marks as values

# student={}
# python=float(input("enter marks of python subject: "))
# student["python"]=python
# java=float(input("enter marks of java subject: "))
# student["java"]=java
# oops=float(input("enter marks of oops subject: "))
# # student["oops"]=oops
# # another update method
# student.update({"oops":oops})

# print(student)


#4. figure out a way to store 9 & 9.0 as separate values in the set.

set={9,"9.0"} #we can store it as a string and int
print(set)

#we can store tuple in a dict
set2={
    ("int",9,
     "float",9.0)
}
print(set2)