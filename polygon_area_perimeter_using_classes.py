"""
Write a test program
that creates three RegularPolygon objects, created using RegularPolygon(),
using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For
each object, display its perimeter and area.

@author: Neha Bais
MET CS-521 A3
"""

import math

class Regular_Polygon():
    # constructor with default values 
    def __init__(self, n = 3, side = 1.0, x = 0.0, y = 0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
        
    # Get the number of sides
    def get_nbr_of_sides(self):
        return self.__n
    
    #gt length of side
    def get_side(self):
        return self.__side
     
    # get x coordinates    
    def get_x_coordinate(self):
        return self.__x
    
    #get y coordinate
    def get_y_coordinate(self):
        return self.__y
    
    #set nbr of sides    
    def set_nbr_of_sides(self, n):
        self.__n = n
    
    #set new length of side
    def set_side(self, side):
        self.__side = side
     
    # set new x coordinate    
    def set_x_coordinate(self, x):
        self.__x = x
    
    #set new y coordinate
    def set_y_coordinate(self, y):
        self.__y = y
     
    #calculate perimter    
    def get_perimter(self):
        return self.__side * self.__n
    
    #calculate area
    def get_area(self):
        return (self.__n * self.__side**2) / (4 * (math.tan(math.pi/self.__n)))
        
    
def main():
    
    case_1 = Regular_Polygon()
    print('\nCase 1: All default vaues')
    print('Perimter of polygon is: ', case_1.get_perimter())
    print('Area of polygon is: ', round(case_1.get_area(), 3))
    
    case_2 = Regular_Polygon(6, 4)
    print('\nCase 2: n = 6 and s = 4')
    print('Perimter of polygon is: ', case_2.get_perimter())
    print('Area of polygon is: ', round(case_2.get_area(), 3))
    
    case_3 = Regular_Polygon(10, 4, 5.6, 7.8)
    print('\nCase 3: n = 10, s = 4, x = 5.6, y = 7.8')
    print('Perimter of polygon is: ', case_3.get_perimter())
    print('Area of polygon is: ', round(case_3.get_area(), 3))    
    
    
    
    
main()    