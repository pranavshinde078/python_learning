 #                                     # program 1

# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
    
# show(5)


 #                      # program 2 call stack concept

# def show(n):
#     if n==0:
#         return
#     print(n)
#     show(n-1)
#     print("call stack",n)
    
# show(5)


 #                          # program 3 factorial

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return factorial(n-1)*n

# print(factorial(5))
        
      
 #                              #  program 5 sum of n numbers
 
# def sum_of_n(n):
#     if n==0:
#         return 0
  
#     return sum_of_n(n-1) + n 

# sum=sum_of_n(5)
# print(sum)

#                                    program 6

movies=['got',"sairat","3 idiots","welcome"]

idx=0
m=len(movies)
def print_movies(movies,idx=0):
    if idx==m:
        return
    print(movies[idx])
    print_movies(movies,idx+1)
    
    
print_movies(movies,idx)
      
                                     
                

