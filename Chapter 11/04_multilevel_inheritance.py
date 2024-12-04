class Employee:
    a=1
    
class Coder(Employee):
    b=2
    
class Programmer(Coder):
    c=3
    
    
p=Programmer()
c=Coder()
a=Employee()

print(a.a)
print(c.a, c.b)
print(p.a, p.b, p.c)