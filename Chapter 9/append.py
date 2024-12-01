path = r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9\file1.txt".replace("//", "\\")

str="I am a winner"
file=open(path,"a")

file.write(str)

file.close()


