import module1
module1.say_hello("pranav")

# to access the specific part/variable from another module

from module1 import person1

print(person1["age"])
print(person1["name"])