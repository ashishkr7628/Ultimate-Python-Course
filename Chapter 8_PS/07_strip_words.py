list=["ish","Ashish","Ramish","Harish","Hari"]

# for i in list:
#     if i=="ish":
#         list.remove(i)
        
    

# print(list)

list1=[]

for i in list:
    if not(i=="ish"):
        list1.append(i.strip("ish"))
print(list1)
        