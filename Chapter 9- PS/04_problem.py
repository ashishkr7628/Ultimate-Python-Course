path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\new_text.txt".replace("//","\\")

with open(path,"r") as f:
    content=f.read()

if "donkey" in content:
    print("donkey is present")
    print(content)
    # newContent=content.replace("donkey","#"*len("donkey"))
    content.replace("donkey","#"*len("donkey"))
    with open(path,"w") as f:
        f.write(content)

else:
    print("donkey is not present")



