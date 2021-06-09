"""
 String Calculator - Implement String calculator with following functions.
• Function that reverses the given string S. (A)
• Function that returns total A’s available (it can be ‘a’ or ‘A’) int given
string S. (B)
• Function that takes 2 inputs string S and index and returns element at
given index. If the index is not available, it should return 0 as the
output. (C)
• Function that multiples given string 5 times (D)
- Implement all the above functions.
- Get input and pass it to the reverse function, get the output from it and call
function C, function C takes 2 params, first param should be output from function
A and second param should be output from function B. Get the output. If the
output is not 0, call function D and print output. Else call print “Completed without
multiply” as the output.
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