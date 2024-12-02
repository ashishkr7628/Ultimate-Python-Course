for i in range(2,21):
    path1=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\tables".replace("//","\\")
    path=path1+f"\multable_{i}.txt"
    print(path)
    table=''
    for j in range(1,11):
        table+=f"{i}X{j}={i*j}\n"
    with open(path,"w") as f:
        f.write(table)
        