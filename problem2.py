#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(c1,c2):
   #i = math.sqrt(((a-x)**2) + ((b-y)**2))
   #return i
   pass
   c1 = tuple(x1,y1)
   c2 = tuple(x2,y2)
   return math.sqrt((x1 -x2)**2 + (y1-y2)**2) 