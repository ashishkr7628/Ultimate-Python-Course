class Employee:
    company="ITC"
    
    def __init__(self):
        print(f"Hello whats up from Employee")
    

class Coder(Employee):
    company="ITC Infotech"
    
    def __init__(self):
        print(f"Hello whats up from Coder")
        
        
a=Employee()
b=Coder()
print(a.company,b.company)
    
    