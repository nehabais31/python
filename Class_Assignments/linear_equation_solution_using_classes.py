# -*- coding: utf-8 -*-
"""
Use Class with private data fields

Write a test
program that prompts the user to enter a, b, c, d, e, and f 
and displays the result.
If is 0, report that “The equation has no solution.”

Test Input :
    No Solution : 1.0,2.0,2.0,4.0,4.0,5.0
    Valid roots : 9.0,4.0,3.0,-5.0,-6.0,-21.0
            x   : -2.0
            y   : 3.0

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
    inp_list = eval(input('Please enter values for a, b, c, d, e, f (separated by comma): '))
    
    a = inp_list[0]
    b = inp_list[1]
    c = inp_list[2]
    d = inp_list[3]
    e = inp_list[4]
    f = inp_list[5]
    
    linear_eq = Linear_Equation(a, b, c, d, e, f)
    
    result = linear_eq.is_solvable()
    if result == False :
        print('The equation has no roots.')
    else:
        x = linear_eq.get_root_1()
        y = linear_eq.get_root_2()
        print('x root is: ', x)
        print('y root is: ', y)
        
main()        