# --------------without list comprension------------

l=[]
for a in range(1,101):
    l.append(a)
    
print(l)

# using list comprehensions

l=[m for m in range(1,101)] #we used m variable for storing iterations
print(l)

#using if
list=[a for a in range(1,101) if a%2==0]#  here a is used for storing values
print(list)

name="pranav"
l=[g for g in name] #string will be converted into a list .for each iteration g var will store the particular value.
print(l)