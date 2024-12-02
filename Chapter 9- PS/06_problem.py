path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\logs.txt".replace("//","\\")

with open(path,"r") as f:
        content=f.readlines()
for lines in content:
    if "python" in lines:
        print("Python is present")
        break
else:
    print("Python is not present")