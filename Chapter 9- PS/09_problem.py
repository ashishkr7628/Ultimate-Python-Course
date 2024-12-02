path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\this.txt".replace("\\","//")

path1=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\newthis.txt".replace("\\","//")

content=""
content1=""
with open(path,"r") as f:
        content=f.read()
with open(path1,"r") as f:
        content1=f.read()
if content1==content:
    print("Content is identical")
else:
    print("Content is not identical")