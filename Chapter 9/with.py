path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9\mytext.txt".replace("//","\\")

file=open(path,"r")
print(file.read())
file.close()

print("---------------------------")

with open(path,"r") as f:
    print(f.read())

