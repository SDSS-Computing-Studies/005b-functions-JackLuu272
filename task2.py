#!python3
"""
##### Task 2
Create a function called largest.
The input is a list.
The return value is the largest value in the list
(2 points)
"""
list = []

n = int(input("Enter numbers of elements: "))
for i in range(0, n):
    elements = float(input())

    list.append(elements)

def largest(list):
    return max(list)

print(max(list))