# -*- coding: utf-8 -*-
"""
Use Class with private data fields

Program that prompts the user to enter the 
endpoints of two line segments
and displays the intersecting point. 


@author: Neha Bais
MET CS-521 A3
"""

class Linear_Equation:
    # Constructing data variables
    def __init__(self, a, b , c, d , e , f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
        
    def get_c(self):
        return self.__c
        
    def get_d(self):
        return self.__d
        
    def get_e(self):
        return self.__e
        
    def get_f(self):
        return self.__f    
    
    # check whether equation has solution or not    
    def is_solvable(self):
        result = (self.get_a() * self.get_d()) - (self.get_b() * self.get_c())
        if result == 0:
            return False
        else:
            return True
    
    # get x root        
    def get_root_1(self):
        numerator = (self.get_e() * self.get_d()) - (self.get_b() * self.get_f())
        denominator = (self.get_a() * self.get_d()) - (self.get_b() * self.get_c())
        
        return numerator / denominator
     
    # get y root    
    def get_root_2(self):
        numerator = (self.get_a() * self.get_f()) - (self.get_e() * self.get_c()) 
        denominator = (self.get_a() * self.get_d()) - (self.get_b() * self.get_c())
        
        return numerator / denominator
    
def main():
    #Input from user
    line_1 = eval(input('Enter coordinates (x1, y1, x2, y2) for first line segement (separated by comma): '))
    line_2 = eval(input('Enter coordinates (x3, y3, x4, y4) for second line segement (separated by comma): '))
    
    # line 1
    x1 = line_1[0]
    y1 = line_1[1]
    x2 = line_1[2]
    y2 = line_1[3]
    
    # line 2
    x3 = line_2[0]
    y3 = line_2[1]
    x4 = line_2[2]
    y4 = line_2[3]
    
    '''
    ax + by = e
    cx + dy = f
    '''
    
    # a b and e values using x and y coordinates
    a = y2 - y1
    b = x1 - x2
    e = a*(x1) + b*(y1)

    # c d and f values using x and y coordinates
    c = y4 - y3
    d = x3 - x4
    f = c*(x3) + d*(y3)
    
    
    linear_eq = Linear_Equation(a, b, c, d, e, f)
    
    result = linear_eq.is_solvable()
    if result == False :
        print('The equation has no intersecting point.')
    else:
        x = linear_eq.get_root_1()
        y = linear_eq.get_root_2()
        print('Intersecting point is :' , x , y)
        
main()        