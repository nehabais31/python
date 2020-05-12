"""
Reverse the input string
using recursive helper function

@author: Neha Bais
MET CS-521 A3
"""

def main():
    string = input('Enter a string: ')
    if len(string) == 0:
        print('You entered a null string')
    else:
        print("Reverse of string is: " , reverse_display(string) )
    
def reverse_display(string):
    '''
    Main recursive function
    to reverse a string
    '''
    return rev_display_helper(string, len(string)-1)
    
def rev_display_helper(string, high):
    '''
    Recursive helper function
    '''
    low = 0
    temp = string[low]
    
    if high <= low :
        return temp  # base case
    else:
        return string[high] + rev_display_helper(string, high-1)  
    

main()        