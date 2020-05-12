# -*- coding: utf-8 -*-
"""
Calculate area and perimter of rectangle 
using class attributes

@author: Neha Bais
MET CS-521 A3
"""

class Rectangle:
    #Constructing the rectangle object
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    
    #Method to calculate perimter of rectangle    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    #MEthod to calculate area of rectangle    
    def get_area(self):
        return self.width * self.height
        
def main():
    
    #REctangle-1
    width_1 = 4
    height_1 = 40
    r = Rectangle(width_1, height_1)
    print('Width of rectangle: ', r.width)
    print('Height of rectangle: ', r.height)
    print('Area of rectangle: ', r.get_area())
    print('Perimter of rectangle: ', r.get_perimeter())
    
    
    #REctangle-2
    width_2 = 3.5
    height_2 = 35.7
    r = Rectangle(width_2, height_2)
    print('\nWidth of rectangle: ', r.width)
    print('Height of rectangle: ', r.height)
    print('Area of rectangle: ', round(r.get_area(),3))
    print('Perimter of rectangle: ', r.get_perimeter())
    
    
main()    
    