"""
Write a recursive function that computes
the sum of the digits in an integer.

@author: Neha Bais
MET CS-521 A3

"""

def main():
    n = eval(input('Input a number: '))
    print('sum of digits of',n, 'is: ', sum_of_digits(n))
    
def sum_of_digits(n):
    '''
    Recursive call of function
    to get the next digit in the
    input number
    
    '''
    if n == 0:
        return 0   # base case
    else:
        return (n % 10 + sum_of_digits(n // 10))

main()        