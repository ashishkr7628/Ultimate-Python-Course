class Employee:
    company="microsoft"
    salary=1800000
    
    def __init__(self,name):
        self.name=name
        print(f" My name is {self.name} and i work in {self.company} and my salary is {self.salary}")
        
    
    
    
ashish=Employee("ashish kumar")
ram=Employee("ram kumar")
hari=Employee("hari kumar")