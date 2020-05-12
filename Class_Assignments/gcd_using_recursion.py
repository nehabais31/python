"""
Created on Thu Apr  9 17:15:09 2020

Test program that prompts the
user to enter two integers and 
displays their GCD using recursive function.

@author: Neha Bais
MET CS-521 A3

"""

def main():
    m = eval(input('Enter first number: '))
    n = eval(input('Enter second number: '))
    print('GCD of ',m,'and', n , 'is: ', gcd(m, n))
    
def gcd(m, n):
    '''
    Recursivefunction to calculate 
    the gcd of 2 numbers
    
    '''
    # check to avoid division by 0
    # if any of the 2 numbers is 0
    if m == 0:      
        return n
    elif n == 0:
        return m
    
    if m % n  == 0:
        return n   # base case
    else:
        return gcd(n, m % n)

main()        