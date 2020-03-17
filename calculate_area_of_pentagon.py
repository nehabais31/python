"""
Neha Bais

Calculating area of Pentagon when user enters legth from centre to vertex

"""

import math

r = eval(input("Enter the length from centre to a vertex : "))   

s = 2 * r * (math.sin(math.pi/5))                       # Calculate side of Pentagon

area = ((3 * (math.sqrt(3)) / 2) * s**2)                # Calculate area of Pentagon 

print ("Area of Pentagon is :", round(area,2))                   