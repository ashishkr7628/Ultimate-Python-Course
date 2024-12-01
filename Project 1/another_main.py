import random

'''
1  -> snake
-1 -> water
0 -> gun

'''

youInp= input("Enter your choice: ")
compInp=random.choice([1, -1, 0])

game={"s":"Snake","w":"Water","g":"Gun"}

gameRev={"s":1,"w":-1,"g":0}

revDict={1:"Snake",-1:"Water",0:"Gun"}

youInt=gameRev[youInp]

print(f"Your choice: {game[youInp]}\n Computer Choice:{revDict[compInp]} ")


if(youInt-compInp==-1 or youInt-compInp==2):
    print("You win")
    
elif(youInt-compInp==0):
    print("Game is drawn")
    
else:
    print("You loose")