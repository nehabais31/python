"""
Created on Thu Apr  2 22:12:36 2020

@author: Neha Bais
MET CS-521 A3

Write a function to sort (in place) the list of numbers as follows:
first positive numbers in increasing order and 
then negative numbers in increasing order

"""

def rearrange_array(x) :
    '''
    Rearranging elements with positive on left 
    and negative on right by doing reverse sort
    '''
    for i in range(len(x)) :
        for j in range(len(x) - 1):
            e_1 = x[j]
            e_2 = x[j + 1]
            if e_1 < e_2 :     # reverse sorting
                x[j] = e_2
                x[j+1] = e_1
    return x    
    
def sort_numbers(x) :
    '''
    Sort the numbers
    '''
    for i in range(len(x)):
        for j in range(len(x) - 1):
            e_1 = x[j]
            e_2 = x[j+1]
            if e_1 > 0 and e_2 > 0 :     # check and sort positive numbers only
                if (e_1 > e_2) :
                    x[j] = e_2
                    x[j+1] = e_1
                    
            elif e_1 < 0 and e_2 < 0 :   # check and sort negative numbers only
                if (e_1 > e_2) :
                    x[j] = e_2
                    x[j+1] = e_1
    return x            
          

def main() :
    x = [2, 6, -6, -3, 1, 19 , -2, -4, -20]
    print('Input Sequence: ', x)
    
    x = rearrange_array(x)
    x = sort_numbers(x)
    
    print('\nSorted Sequence:', x)

    
main()  