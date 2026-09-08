
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
s1=Student("pranav",50)
print(s1.name,s1.marks)

del s1.name
print(s1.name)
print(s1.marks)
del s1
print(s1)


#                   program 2program for private attributes


# class Student:
#     def __init__(self,name,marks):
#         self.__name=name
#         self.__marks=marks
     
      
#     def reset_name(self):
#         print(self.__name)  #this will not throw an error becoz we are using a __name attribute in a same class
        
# acc1=Student("pranav",100)
# print(acc1.reset_name())
# print(acc1.__name)  #this will throw error bcz __name is a private attribute


#                               program 3


# class Person:
#     __name="anonymous"
    
#     def __hello(self):
#         print("Hello.......")
    
    
      
# p1=Person()
# print(p1.__hello())       


#                               program 4


# class Person:
#     __name="anonymous"
    
#     def __hello(self):
#         print("Hello.......")
    
    
#     def welcome(self):
#         self.__hello()
      
# p1=Person()
# p1.welcome()


#                           program 5
