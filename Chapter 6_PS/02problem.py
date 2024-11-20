sub1= int(input("Enter first subject: "))
sub2= int(input("Enter second subject: "))
sub3= int(input("Enter third subject: "))

if(((sub1+sub2+sub3)/3)>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print("Pass")
else:
    print("Fail")