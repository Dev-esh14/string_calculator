"""
 You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
"""

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