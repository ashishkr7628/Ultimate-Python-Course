l1= [1,8,7,2,21,15]

l1.sort()
# arrange the list in ascending order

print(l1)

l1= [1,8,7,2,21,15]

l1.reverse()
#  reverse the order of the list
print(l1)

l1.append(5)
# add value 5 at the end of list
print(l1)

l1= [1,8,7,2,21,15]
l1.insert(2,111)
# insert the value 111 at 2 index of the list

print(l1)


l1.pop()
# it dont give any arguments in the pop method it will take as it last index
# returns last index
print(l1)

l1.pop(2)
# argument in the pop method tells which index you have to delete
# returns removed index
print(l1)


l1.remove(21)
# argument given in the remove tells which value you have remove from the list


print(l1)

l2=[4,4,5,5,4,3,2,1]

print(l2.count(4))
# count methods return the no. of occurrence of that value inside the list