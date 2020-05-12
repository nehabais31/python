# -*- coding: utf-8 -*-
"""
Write a test program that prompts the user to enter a phone number as a string. 
The input number may contain letters. The program translates a letter 
(uppercase or lowercase) to a digit and leaves all other characters intact.

@author: Neha Bais
MET CS-521 A3
"""

# mapping key's numbers to letters
def get_phone_nbr(user_inp):
    map_letters = {
        'a' : 2,
        'b' : 2,
        'c' : 2,
        'd' : 3,
        'e' : 3,
        'f' : 3,
        'g' : 4,
        'h' : 4,
        'i' : 4,
        'j' : 5,
        'k' : 5,
        'l' : 5,
        'm' : 6,
        'n' : 6,
        'o' : 6,
        'p' : 7,
        'q' : 7,
        'r' : 7,
        's' : 7,
        't' : 8,
        'u' : 8,
        'v' : 8,
        'w' : 9,
        'x' : 9,
        'y' : 9,
        'z' : 9 
    }
    
    input_list = list(user_inp)
    
    for i, c in enumerate (input_list ):
        if c.lower() in map_letters :
            input_list[i] = str(map_letters[c.lower()])
    return ''.join(input_list)  
           

def main():
    user_inp = input('Enter a string: ')
        
    print('Phone number: ', get_phone_nbr(user_inp))
    
main()    
    