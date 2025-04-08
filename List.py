list1 = [1, 2, 3]
list2 = list1 #Shallow copy, only reference not a copy of object
list2.append(4)
print(list1)

#[1,2,3,4]
