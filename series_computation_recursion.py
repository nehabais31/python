"""
(Sum series) Write a recursive method to compute the following series:         
                                                                              
m(i) = 1 / 3 + 2 / 5 + 3 / 7 + 4 / 9 + 5 / 11 + 6 / 13 + ... + i / (2i + 1)  

@author: Neha Bais
MET CS-521 A3

"""

def main():
    '''
Series:  1 / 3 + 2 / 5 + 3 / 7 + 4 / 9 + 5 / 11 + 6 / 13 + ... + i / (2i + 1)
    '''
    i = 10
    
    print(main.__doc__)
    print("Sum of series is: " , round(sum_of_series(i) , 4) )
    
def sum_of_series(i):
    '''
    Recursive function to compute 
    the sum of series
    '''
    
    if i == 0 :
        return 0    # base case
    else:
        return  i / (2 * i + 1) + sum_of_series(i - 1)   

main()        