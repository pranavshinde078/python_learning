# import random
# import string

# pass_len=12
# charvalues=string.ascii_letters+string.digits+string.punctuation

# password=""
# for i in range(pass_len):
#     password+=random.choice(charvalues)
    
# print("your random password is :-",password)
    
    
    
    
                        # program 2 using list comprehension
                        
                        
import random
import string

charvalues=string.ascii_letters+string.digits+string.punctuation
pass_len=8
password="*".join([random.choice(charvalues) for i in range(pass_len)])

print(f"your random password is :- {password}")