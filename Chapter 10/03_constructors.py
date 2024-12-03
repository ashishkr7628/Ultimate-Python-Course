#  __int__ - this function is called dunder function in python
class Employee:
    language="c++"
    salary=1300000
    #  this is constructor in python which is going to be called at the time of object creation
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"Object has been created for {self.name} and his age is {self.age}")
        
    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
    
    def getMoreInfo(self):
        print("This section gives more information about me")
    
    @staticmethod    
    def greet():
        print("Good morning")
        
    # static method is a decorator is used when we dont want to pass the self parameter and it will be part of class and can be called using Class name
    
ashish= Employee("Ashish",23) 
      

