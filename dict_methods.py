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

