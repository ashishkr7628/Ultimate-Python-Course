class Employee:
    
    name="Ashish"
    company="Google"
    
    def showDesc(self):
        print(f"Hello I am {self.name} and i work in {self.company}")
        
class Coder:
    
    language="python"
    
    def showDefination(self):
        print(f" I know about programming language {self.language}")
        
        

class Programmer(Coder,Employee):
    def show(self):
        print(f"My name is {self.name} and i work in {self.company} and i am familiar with {self.language}")
        

a=Programmer()

a.show()
a.showDefination()
a.showDesc()