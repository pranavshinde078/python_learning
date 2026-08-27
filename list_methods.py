marks=[60,40,80,90,100,40,47,63]
print("original list",marks)

print(marks.append(88))
marks.append(22)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

print(marks.insert(0,10))
print(marks)

marks.reverse()
print(marks)

marks.remove(40)#removes first occurence of 40
print(marks)

marks.pop(0)
print(marks)

marks.clear()
print(marks)

#sorting also applies on string values in list

# flowers=["sunflower","rose","marigold","lotus","aaaa","bbbb"]

# print(flowers.sort())
# print(flowers)

# print(flowers.sort(reverse=True))
# print(flowers)

# flowers.sort()
# print(flowers)

