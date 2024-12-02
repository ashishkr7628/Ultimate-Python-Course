path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\new_text.txt".replace("//","\\")


    
words=["donkey","ganda","gadha"]
for word in words:
    with open(path,"r") as f:
        content=f.read()
    if word in content:
        print(f"{word} is present")
    print(content)
    # newContent=content.replace("donkey","#"*len("donkey"))
    newContent=content.replace(word,"#"*len(word))
    with open(path,"w") as f:
        f.write(newContent)



