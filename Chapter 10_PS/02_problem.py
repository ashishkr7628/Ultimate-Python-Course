class Calulator:
    
    def __init__(self,n):
        self.n=n
        
    
    
    def square(self):
        print(self.n*self.n)
        
    def cube(self):
        print(self.n*self.n*self.n)
        
    def squareroot(self):
        print(self.n**1/2)
        
        
        
calulate= Calulator(4)
calulate.square()
calulate.squareroot()
calulate.cube()