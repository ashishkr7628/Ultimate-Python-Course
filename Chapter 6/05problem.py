substring="Hello ashish how are you?"
name= input("Enter your name: ")


if(name.lower() in substring.lower()):
    print("Present")
else:
    print("Not present")