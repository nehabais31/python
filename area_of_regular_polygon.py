"""
Neha Bais

Calculating area of a regular Polygon

"""

import math

n = eval(input("Enter number of sides of Poygon :"))
s = eval(input("Enter the length of side :"))

area = (n * s**2) / (4 * math.tan(math.pi/n))

print ("Area of Polygon is :", round(area,2))