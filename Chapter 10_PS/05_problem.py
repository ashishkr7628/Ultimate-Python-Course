from random import randint
class Railway:
    
    
    def __init__(self,no,fro):
        self.n=no
        self.fro=fro
        print("Ticket has been generated")
    
    def getStatus(self):
        print(f"The train with trainNo. {self.n} is running successfully")
    
    def getFare(self):
        
        
        print(f"The train with trainNo. {self.n} having price {randint(222,5555)} ")
        
    
    def getTicket(self):
        print(f"The train with trainNo. {self.n} is running from {self.fro} ")



ticket1=Railway(127801,"Delhi")
ticket1.getFare()        
ticket1.getStatus()        
ticket1.getTicket()        