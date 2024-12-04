class Employee:
    a = 10

    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
        
    @property    
    def name(self):
        return f"{self.fname} {self.lname}"
    
    
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]



a = Employee()
a.a = 45  # This does not affect the class variable 'a'
a.show()  # Outputs: The value of a is 10
a.name="Ashish Kumar"

print(f"First name: {a.fname}, Last name : {a.lname}")

