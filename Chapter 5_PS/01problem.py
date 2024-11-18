meanings={
    "madad":"help",
    "khana":"khana",
    "sona":"sleep",
    "pani":"water"
}


user=input("Enter the word you want to know their meanings: ")

print(meanings.get(user))
