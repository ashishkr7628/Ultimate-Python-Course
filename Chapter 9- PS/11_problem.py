path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\this.txt".replace("\\","//")
path1=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\renamed_by_python.txt".replace("\\","//")


with open(path,"r") as f:
        content=f.read()
with open(path1,"w") as f:
        f.write(content)