"""
Created on Thu Apr  2 23:37:29 2020

@author: Neha Bais
MET CS-521 A3

Write a function complementary(x, y)
that take as input two DNA sequences 
(encoded as strings, same length) 
and returns True if these sequences 
are complementary.

"""


def  calculate_complementary_seq(x) :
    '''
    Computing complementary sequence of input
    string and then reversing it
    '''
    x_list = list(x)
    x_complementary = []   # Empty list to store complementary sequences

    # Mapping each DNA seq to its complementary
    for e in x_list :
        if e == 'A' :
            x_complementary.append('T')
        elif e == 'T' :
            x_complementary.append('A')
        elif e == 'C' :
            x_complementary.append('G')
        elif e == 'G' :
            x_complementary.append('C')
    
    # reverse the computed complementary sequence    
    x_complementary =  x_complementary[ :  : -1] 
    
    # converting list to string
    x_complementary = ''.join(x_complementary)
    
    return x_complementary


def check_complementary(x , y):
    '''
    Checking whether the computed coplementary
    string returned by compute function is same
    as other input string
    '''
    x_complementary = calculate_complementary_seq(x)
    if x_complementary == y :
        return True
    else :
        return False
    
def main() :
    x = 'TTAC'
    y = 'GTAA'
    
    if (x.isalpha() and y.isalpha()) and (len(x) == len(y)) :
        result = check_complementary(x, y) 
        if result == True :
            print(x ,'and', y , 'are complementary to each other.')
        else :
            print(x ,'and', y , 'are not complementary to each other.')
    else :
        print(x,'and',y,'are not valid to check')            
        
main()        
