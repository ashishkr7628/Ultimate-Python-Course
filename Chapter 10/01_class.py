class Employee:
    # It is a class attribute
    language="Py"
    salary=1250000
    
Ashish= Employee()
# It is a object/instance variable
Ashish.name="Ashish Kumar"
Ashish.age=25


Rohan=Employee()
Rohan.name="Rohan Ojha"
Rohan.age=22

print(Ashish.language,Ashish.salary,Ashish.name,Ashish.age)

#  we can change the class attribute value or ovveride it


Ashish.language="Java"
Ashish.salary=1300000

print(Ashish.language,Ashish.salary,Ashish.name,Ashish.age)
print(Rohan.language,Rohan.salary,Rohan.name,Rohan.age)
