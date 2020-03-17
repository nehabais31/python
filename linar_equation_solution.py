"""
Neha Bais

Solve 2 * 2 linear equation using Cramer's Rule

"""

a,b,c,d,e,f = eval(input("Enter values for a,b,c,d,e,f :"))

if (a * d) - (b * c) == 0 :
   print ("The equation has no solution.")
else :   
   x = (e * d - b * f) / (a * d - b * c)
   y = (a * f - e * c) / (a * d - b * c)
   print ("x is " , round(x,3) , "and y is" , round(y,3))   