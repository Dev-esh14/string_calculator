def reverse(str):
    return str[::-1]
    
def total_a(b):
    l=list(b)
    count=0
    if 'a' in list(b):
        count=count+1
        return count
    elif 'A' in list(b):
        count=count+1
        return count
    else:
        count=0
        return count

def index(b,c):
    if c==0:
        return 0
    else:
        l=list(b)
        element=l.pop(c)
        return element

def multiply(output):
    return output*5
    
str=input("enter the string:")
b=reverse(str)
c=total_a(b)
output=index(b,c)
print(output)
print(multiply(output))

"""
OUTPUT:
enter the string:hari
r
rrrrr
"""