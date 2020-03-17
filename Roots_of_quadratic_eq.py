"""
Neha Bais

Script to find the roots of quadratic equation 

"""

import math

a,b,c = eval(input("Enter the value for a,b and c :"))

discriminant = b**2 - (4 * a * c)

if discriminant == 0 :
   r = -b / (2 * a)
   print ("The root is : ", r)
elif discriminant > 0 :
   r1 = (-b + math.sqrt(b**2 -4 * a * c)) / (2 * a)
   r2 = (-b - math.sqrt(b**2 -4 * a * c)) / (2 * a)
   print ("The roots are : ", r1 ,"and", r2)
else :
   print ("The equation has no real roots")