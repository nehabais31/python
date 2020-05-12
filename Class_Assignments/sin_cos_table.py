"""
Neha Bais

Print the following table to display the sin value
and cos value of degrees from 0 to 360 with increments of 10 degrees. Round the
value to keep four digits after the decimal point.
Degree   Sin      Cos
0       0.0000   1.0000
10      0.1736   0.9848
...
350    -0.1736   0.9848
360     0.0000   1.0000

"""

import math

# degree from 0 to 360 with increment of 10
degree = [e for e in range(0,361,10)]

# list storing all the sin values
sin_value = [math.sin(math.radians(e)) for e in degree ]

# list storing all the cos values
cos_value = [math.cos(math.radians(e))  for e in degree ]

# printing loop
print('Degree \t\t Sin \t\t Cos')
for i in range(len(degree)) :
    print( degree[i] , '\t\t' , format(sin_value[i], '.4f') ,\
    '\t' , format(cos_value[i], '.4f') )           