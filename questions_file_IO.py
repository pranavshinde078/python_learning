#                   program 1

# create a new file practice.txt using Python.add the following data in it

# Hi everyone
# we are learning File I/O
# using Java.
# i like programming in Java.

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java.")
#     f.write("\ni like programming in Java.")


#                   program 2

# WAF to override the occurences of "Java" with "Python" in above file

# with open("practice.txt","r") as f:
#     data=f.read()
    
# new_data=data.replace("Java","Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)


#                   WAP to find the learning word exist in file or not

# with open("practice.txt","r") as f:
#     data=f.read()
    
#     if data.find("learning") !=-1:
#         print("found")
#     else:
#         print("not found")

# with open("practice.txt","r") as f:
#     data=f.read()
    
#     if data.find("learning") !=-1:
#         print("found")
#     else:
#         print("not found")


#           WAF to check the word "learning" exist int the file & return its line no. if does not exist return -1


def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline() #f.readline() returns "" when file ends so it stops working
            if(word in data):
                
                return line_no
            line_no+=1
    return -1

print(check_for_line())
    