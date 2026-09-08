
class Person:
    name="anonymous"
     
    def changeName(self,name):
        self.name=name
        #Person.name #this will change the class attribute value
        #self.__class__.name="rahul" # this will also change the class attribute value
        
p1=Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)# class attribute value will not be changed


#               program for changing class attributes using class methods

# class Person:
#     name="anoymous"
    
#     @classmethod
#     def changeName(cls,name):  #cls refers to the class
#         cls.name=name
        
# p1=Person()
# p1.changeName("rahul")
# print(p1.name)
# print(Person.name)