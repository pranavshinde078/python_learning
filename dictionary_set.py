# info={
#     "name" : "pranav",
#     12 : 50.55,
#     "subjects" : ["os","cn","oop","dbms"],
#     "marks": [50,60,50,40,80],
#     "is_men":True
    
    
# }
#uodate
# info["is_men"]=False

# print(info)
# print(info["name"])
# #assign
# info["surname"]="shinde"
# print(info["surname"])

# null_dict={}

# null_dict["name"]="pranavs"
# print(null_dict)

# NESTED DICTIONARY

students={
    "name":"pranav",
    "subjects":{
        "phy":40,"chem":50,"marathi":60
    }
        
}

print(students)

print(students["name"])
print(students["subjects"]["chem"])