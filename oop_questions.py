# WAP to create Student class that takes name & marks of 3 subjects as a arguments in constructor. then creat a method to print the avg

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
    
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("HI",self.name,"your average is",sum/3)
        
        
# s1=Student("pranav",[50,40,60])
# s1.get_avg()


#     #   changing the object attribute
# s1.name="satyajeet"
# s1.get_avg()


#                       Static methods 

# class Car:
#     @staticmethod
#     def hello():
#         print("hello pranav")
        
# c1=Car()
# c1.hello()


#                   program for bank account managment


class Account:
    
    def __init__(self,bal,acc_no):
        self.account_no=acc_no
        self.balance=bal
      
    def credit(self,amount) :
        self.balance+=amount
        print("Rs ",amount,"was credited")
        print("your total balance is",self.balance_amount())
        
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs ",amount,"was debited")
        print("your total balance is",self.balance_amount())
     
    def balance_amount(self):
        return self.balance   
        
account1=Account(50000,1)
print("account no.",account1.account_no)
print("current balance",account1.balance)


account1.debit(10000)
account1.credit(10000)

print("\n****  account 2*****\n")
account2=Account(1000,2)
print("account no.",account2.account_no)
print("current balance",account2.balance)


account1.debit(10000)
account1.credit(10000)