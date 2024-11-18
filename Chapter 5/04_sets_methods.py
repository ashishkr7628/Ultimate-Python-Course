s={1,8,2,3}

# len() this will return the length of the set

print(len(s)) 

# remove() this method will take argument which is the value which is to be deleted.

print(s.remove(2))
#  remove method will return as None


s.pop()
#  it remove the abriatary value from the set

print(s)


s.clear()

#  it will remove all the elements from the set

print(s)


m={1,4,2,6,3,8,11}

# print(m.union({8,11}))
#  union() will take set as argument and include the set with the original set without duplicates


print(m.intersection({8,11}))

#  it will return the None nothing matches if matches then return the set

print(m.difference({8,11}))
# it will return the set with excluded values from the set from which it is compared


