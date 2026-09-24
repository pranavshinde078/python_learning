import random

target=random.randint(1,100)


while True:
    userchoice=input("enter your guess (1-100) or quit :- ")
    
    
    if userchoice.lower()=="quit":
        print("end ")
        break
    
    userchoice=int(userchoice)
    if userchoice==target:
        print("Correct guess !")
        break
    
    elif userchoice < target:
        print("your guess is small , guess bigger Number! :")
        
    else :
        print("your choice is larger , guess the smaller number !")
        
print("-----------game over-------------")