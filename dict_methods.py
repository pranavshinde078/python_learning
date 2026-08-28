student={
    "name":"pranav",
    "age":19,
    "subjects":"chem"
}


print(student.keys())

print(student.values())

#to convert dict type to list type
print(list(student.keys()))
print(list(student.values()))

#this returns key value pairs as tuples
print(student.items())

print(list(student.items()))

#to access values like an index first we have to convert it to list type
pairs=list(student.items())
print(pairs[0])

# to access the value of the key

print(student.get("name2"))

# print(student["name2"]) this statement will give error bcz name 2 key doesnt exit but .get method will simply return none without crashing the program
#  update dict
student.update({"city":"pune"})
print(student)
# second option to update
new_dict={
    "address":"delhi"
}
student.update(new_dict)
print(student)

