"""
Write a recursive function that displays
a string reversely on the console

inp : abcd
out : dcba

@author: Neha Bais
MET CS-521 A3
"""

def main():
    inp_str = input('Enter a string: ')
    if len(inp_str) == 0:
        print('You entered a null string')
    else:
        print("Reverse of string is: " , reverse_display(inp_str) )
    
def reverse_display(inp_str):
    
    i = len(inp_str) - 1   
    
    if i == 0 :
       return inp_str[len(inp_str)-1]  # base case, return last char
    else:
       return inp_str[i] + reverse_display(inp_str[0 : i])  
    
main()        