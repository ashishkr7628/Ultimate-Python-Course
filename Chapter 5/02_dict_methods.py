student={
    "name": "Ashish",
    "class":"12B",
    "roll":25,
    "marks":{
        "maths":50,
        "physics":60,
        "chem":80
    },
    
    
    
    
    
}


# methods in dictionary

# print(student.items())
#  it will return the list of tuples containing key and values

print(student.keys())
#  it will return the list of keys

student.update({"name":"Ashish Kumar","roll":100})
student.update(roll=101)
student.update(hobby="playing cricket")
student.update([("age",25)])
# print(student["name"])
# print(student["roll"])
# print(student)

# in update method we can give argument in three ways
# -> pass the dictionary containing keys and values if it is already there it will override otherwise it will create and add one
# --> by passing the direct value, variable and value
#--> pass the list of tuples containing keys and value


print(student.get("name"))
print(student["name"])

print(student.get("roll1"))
# print(student["roll1"])

#  difference between dict.get() and dict[] it will get the same value if the key exists otherwise get() will give None and [] will give error

a={}
#  empty dictionary is denoted as this.


print(type(a))
