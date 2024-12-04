class Employee:
    company="Microsoft"
    address="Bangalore"
    
    
class Programmer(Employee):
    
    def __init__(self,name):
        print(f"My name is {name} and i work in {self.company} and live in {self.address}")
        
        
ashish=Programmer("Ashish Kumar")