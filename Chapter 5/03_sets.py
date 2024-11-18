# set is just like list or tuple to store data but we cannot store duplicate data


a=set() 
# empty set can be created like this

#  it also has {} like dictionary

a.add(1)
a.add(2)
a.add("Ashish")
a.add(True)
a.add(None)
# a.add(False)
#  here 1==True
# 0==False


print(a)

b={5,"5",123,"Ashish",5.0}

print(b)
# 5 and "5" are taken as different but 5 and 5.0 are same because of the values.

