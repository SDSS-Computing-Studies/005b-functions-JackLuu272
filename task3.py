#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

list = []

n = int(input("Enter the number of elements: "))

for i in range (0, n):
    elements = float(input())

    list.append(elements)

def perimeter(list):
    return sum(list)

print(sum(list))
    