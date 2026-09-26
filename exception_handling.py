# num=input("enter a number :- ")

# try:
#     print(f"multiplication table of {num} :- ")
#     for i in range(1,11):
#         print(f"{int(num)} x {i}={int(num)*i}")
    
# except:
#     print("some error occured !")
    
# print("end of the program!")


#                               ------program 2---------


# try:
#     num=int(input("enter the number :-"))
#     a=[5,6,7]
#     print(a[num])
    
# except ValueError:
#     print("entered number is not an integer !")

# except IndexError:
#     print("index error")
    
    
    #                           ----program 3-----------
    

# num1=input("enter the  first number :-")
# num2=input("enter the  second number :-")

# try:
#     print(int(num1)/int(num2))
    
# except ValueError:
#     print("enter integer values only !")
    
# except ZeroDivisionError:
#     print("cannot divide by zero !")
    
    # ----------------program 4-----------
    
try:
    result="10"+10
    
except TypeError:
    print("cannot add string with int !")
    
student={"name":"pranav",
         "age":20,
         "marks":90}

try:
    print(student["name"])
    print(student["subject"])
    
except KeyError:
    print("the key doesn't exist ")
    
try:
    print(x)
    
except NameError:
    print("x is not defined !")
    

try:
    open("file_io.pyd")
    
except FileNotFoundError:
    print("file not found !")
    
try:
    name="pranav"
    name.append("shinde")   #append i used only with lists
    
except:
    print("string dont support append !")
    
else:
    print("code ran without exception !")
    
finally:
    print("end of the code !")