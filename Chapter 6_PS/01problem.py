user1= int(input("Enter the first no. "))
user2= int(input("Enter the second no. "))
user3= int(input("Enter the third no. "))
user4= int(input("Enter the fourth no. "))


if(user1>user2 and user1>user3 and user1>user4):
    print("The greatest no. ",user1)
elif(user2>user1 and user2>user3 and user2>user4):
    print("The greatest no. ",user2)
elif(user3>user2 and user3>user1 and user3>user4):
    print("The greatest no. ",user3)
# elif(user4>user2 and user4>user3 and user4>user1):
#     print("The greatest no. ",user4)
else:
     print("The greatest no. ",user4)
    