# f=open("set_methods.py","rt")
# data=f.read()
# print(data)
# print(type(data))

# f.close()


#               # program to read only first five letters
# f=open("set_methods.py","rt")
# data=f.read(5)
# print(data)
# print(type(data))

# f.close()

                # program to read line by line
                
# f=open("set_methods.py","rt")
# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# f.close()


#                        program for writing to the file


# f=open("demo.txt","w")
# f.write("i love coding")
# f.close()


#                        program for appending to the file


# f=open("demo.txt","a")
# f.write("\ni love coding")
# f.close()

#overrides the data from  start
# f=open("demo.txt","r+")
# f.write("abc")

# f.close()



#                       deleting a file using os module

import os
os.remove("demo2.txt")