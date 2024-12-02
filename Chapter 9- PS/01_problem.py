path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\poem.txt".replace("//","\\")


with open(path) as f:
    data=f.read()
    if "twinkle" in data:
        print("twinkle is present")
    else:
        print("twinkle is not present")
        
    
        