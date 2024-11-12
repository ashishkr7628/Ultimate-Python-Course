letter= ''' Dear <|NAME|>,
            You are Selected!
            <|DATE>'''
            
print(letter)

print(letter.replace("<|NAME|>","Ashish").replace("<|DATE>","12 Nov"))