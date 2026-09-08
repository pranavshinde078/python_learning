
#               program single level inheritance


class Car:
    @staticmethod
    def start():
        print("car started....")
        
    @staticmethod
    def stop():
        print("car stopped....")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
# car1=ToyotaCar("Fortuner")
# print(car1.name)
# print(car1.start()) # ToyotaCar class inherited all the properties of the class Car


#               program 2 multilevel inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("car started....")
        
#     @staticmethod
#     def stop():
#         print("car stopped....")
        
# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand
  
# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type=type
    
    
      
# car1=Fortuner("diesel")
# car2=ToyotaCar("toyota")
# print(car2.brand)
# print(car1.start())


#                       program 3 

# class A:
#     varA="welcome to place A"
    
# class B:
#     varB="welcome to place B"
    
# class C(A,B):
#     varC="welcome to place C"
    
# c1=C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)