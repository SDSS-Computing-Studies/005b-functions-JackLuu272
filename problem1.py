#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""

def hypotenuse(a,b):
    if a**2 + b**2 == c**2:
        return c 
    elif a**2 + b**2 != c**2 and a > b:
        return a
    else:
        return b 