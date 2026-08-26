marks=float(input("enter your marks in percentage : "))

if (marks>=90 and marks<=100):
    print("grade :- 'A'")
 
elif (marks>=80 and marks<90):
    print("grade :- 'B'")
    
elif (marks>=70 and marks<80):
    print("grade :- 'C'")
    
elif (marks>=40 and marks<70):
    print("pass")   
    
elif (marks<40 and marks >=0):
    print("fail")
