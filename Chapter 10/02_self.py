class Employee:
    language="c++"
    salary=1300000
    
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def getMoreInfo(self):
        print("This section gives more information about me")
    
    @staticmethod    
    def greet():
        print("Good morning")
        
    # static method is a decorator is used when we dont want to pass the self parameter and it will be part of class and can be called using Class name
    
        
        
ram=Employee()
Employee.greet()
ram.getInfo()
ram.getMoreInfo()
