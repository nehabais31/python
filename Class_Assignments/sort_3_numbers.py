"""
Created on Thu Apr  2 10:11:42 2020

@author: Neha Bais
MET CS-521 A3

prompts the user to enter three numbers and invokes the
function to display them in increasing order

"""

def displaySortedNumbers(num1, num2, num3):
    '''
    Sort numbers in increasing order
    '''
    numbers = [num1, num2, num3]
    numbers.sort()
    print('The sorted numbers are: ', end = ' ')
    for e in numbers:
        print( e , end = ' ')

def main():
    num1, num2, num3 = eval(input('Enter 3 numbers separated by comma: '))
    displaySortedNumbers(num1, num2, num3)
    
main()
    
