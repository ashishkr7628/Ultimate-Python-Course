path = r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9\mytext.txt".replace("\\", "/")
file=open(path,"r")

# print(file.readline())
# print(file.readline())
# print(file.readline())

line=file.readline()

while(line!=""):
    print(line)
    line=file.readline()

# print(file.readlines(),type(file.readline()))

file.close()