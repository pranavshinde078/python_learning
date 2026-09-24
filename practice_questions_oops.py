# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     #area of a circle    
#     def Area(self):
#         return 3.14*self.radius**2
    
#     #perimeter of a circle
#     def perimeter(self):
#         return 2*3.14*self.radius
    
# c1=Circle(21)0
# print(c1.Area())
# print(c1.perimeter())
        
        
                            #inheritance
                            
        
        
# class Employee:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
        
#     def Show_details(self):
#         print("Role :-",self.role)
#         print("Department :-",self.department)
#         print("Salary :-",self.salary)
        
        
# # e1=Employee("Manager","Finance","50000")
# # print(e1.Show_details())


# class Engineer(Employee):
#     def __init__(self,name ,age):
#         self.name=name
#         self.age=age
#         super().__init__("manager","software development","50000")
        


# engg1=Engineer("pranav",20)
# engg1.Show_details()


                                #dunder functions
                                
                                
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self, ord2):
        return self.price > ord2.price # if we dont write dunder then it will give an error
    
ord1=Order("banana",30)
ord2=Order("tea",15)       

print(ord1 > ord2) 
        
        