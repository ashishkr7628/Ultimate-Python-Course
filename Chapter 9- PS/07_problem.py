path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\logs.txt".replace("//","\\")

with open(path,"r") as f:
        content=f.readlines()
line=1
for lines in content:
    if "python" in lines:
        print(f"Python is present in line: {line}")
        line+=1
    else:
        line+=1    
else:
    print("Python is not present")