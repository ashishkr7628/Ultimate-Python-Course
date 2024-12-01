# greatest of 3 no.

def greatest(a,b,c):
    if a>b and a>c:
        return a
    
    elif b>c and b>a:
        return b
    
    else:
        return c
    
print(greatest(3,45,34))

def highest(a,b,c):
    
    return max(a,b,c)

a=highest(3,10,50)

print(a)


    
    