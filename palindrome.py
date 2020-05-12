"""
Created on Wed Apr  1 17:28:42 2020

@author: Neha Bais
MET CS-521 A3

program that prompts the
user to enter an integer and reports whether the integer is a palindrome.

"""

def reverse(number) :
    '''
    Get the reverse of input number
    '''
    x = str(number)
    reverse_number = int(x[ : : -1])
    return reverse_number
    
    
def isPalindrome(number) :    
    '''
    Check whether the input number is a Palindrome 
    '''
    reverse_number = reverse(number)
    if number == reverse_number :
        return True
    else :
        return False


def main() :
    '''
    main function
    '''
    number = eval(input('Enter a number: '))

    palindrome = isPalindrome(number)
    if palindrome :
        print('Number' , number, 'is a Palindrome.')
    else :
        print('Number', number , 'is not a Palindrome.')

main()

    