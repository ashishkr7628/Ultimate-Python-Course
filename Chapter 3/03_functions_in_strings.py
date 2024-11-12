# functions in strings

name="Ashish"

# ḷen() is used to find the length of the string

print(len(name))

# str() is used to convert the object into string

print(str(name))

# 
# str_.endswith() is check whether the string ends with this or not

# print(name.endswith("sh"))
# print(name.endswith("shi"))


# startswith() check whether the string is starts with this or not

print(name.startswith("As"))
print(name.startswith("as"))


# capitalize() is used to capital the first character of the string


str= "ashish is my name"

print(str.capitalize())


print('****************')

# count() is used to find no. of occurence if that substring

# print(str.count("a"))
# print(str.count("s"))
# print(str.count("is"))
# print(str.count("my"))
# print(str.count("my name"))

# find() gives the index of the first occurred substring

# print(str.find("i"))
# print(str.find("ish"))
# print(str.find("name"))



# replace() fucntion takes two argument, first which is to be replaced and second which will replaced it

print(str.replace("ashish","shyam"))