# prime number

num = int(input("Enter a number: "))
flag=True
for i in range(2,num):
    if num%i==0:
        flag=False
        print("Not Prime")
        break
if flag==True:
    print("Prime")
