class Employee:
    def __init__(self):
        print("Welcome to Employee page")
    
class Coder(Employee):
    def __init__(self):
       print("Welcome to Coder page")
    
    def showCoder(self):
        super().__init__()
        print("Hello Employee")
    
class Programmer(Coder):
    
    def __init__(self):
       
        print("Welcome to Programmer page")
    
    def showProgrammer(self):
        super().__init__()
        print("Hello Programmer")
    
    
# p=Programmer()


# p.showCoder()

a=Coder()
a.showCoder()


