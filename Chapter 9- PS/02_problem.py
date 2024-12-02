import random

path=r"C:\Users\ASHISH\Desktop\Ultimate Python Course\Chapter 9- PS\Hiscore.txt".replace("//","\\")

def game():
   val_input=random.randint(1,62)
   
   with open(path,"r") as f:
       score=f.read()
       hiscore=0
       if score=="":
           hiscore=0 
       else:
           if val_input >int(score):
               hiscore=val_input
           else:
               hiscore=score
   print(val_input)
   with open(path,"w") as f:
       f.write(str(hiscore))
   
game()       
    
    
