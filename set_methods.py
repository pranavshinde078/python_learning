# # set ignores duplicate values
# collection=set()
# collection.add(2)
# collection.add(2)
# collection.add(2) 
# collection.add("ps")
# collection.add(2)
# print(collection)

# print("length is ",len(collection))

# collection.remove("ps")
# print(collection)


# #  we can add tuple in the set bcoz tuple also are immutable but we cant add list / dict in set bcoz they are mutable
# collection.add((50,10,80,40,50,60,3))
# print(collection)

# # collection.remove(7)  #error becoz 7 does not exist

# collection.clear()
# print(collection)

set1={10,20,30,4,45,0}
set2={10,20,60,80}

print(set1.pop()) #pop removes random element from the set
print("set1",set1)
print("set2",set2)

print("set union",set1.union(set2))

print("set intersection",set1.intersection(set2))