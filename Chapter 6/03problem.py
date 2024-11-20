str1= "make a lot of money"
str2="subscribe"
str3="click this"
str4="buy now"


spam_msg= input("Enter your message: ")

if(str1 in spam_msg):
    print("Spam message")
elif(str2 in spam_msg):
    print("Spam message")
elif(str3 in spam_msg):
    print("Spam message")
elif(str4 in spam_msg):
    print("Spam message")
else:
    print("Not a spam message")