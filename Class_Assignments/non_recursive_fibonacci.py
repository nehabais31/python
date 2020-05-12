"""
Non-recursive function to 
compute fibonacci number of 
input index

@author: Neha Bais
MET CS-521 A3
"""

def main():
    n = eval(input('Enter an index: '))
    print("Fibonacci of", n , "is: " , fibonacci(n) )
    
def fibonacci(n):
    '''
    Non-recurssive function to generate
    fibonacci number of input index
    '''
    if n <= 2:
        return 1
    else:
        fib_0 = 0
        fib_1 = 1
        
        for i in range(2, n + 1):
            current_fib = fib_0 + fib_1
            fib_0 = fib_1
            fib_1 = current_fib
            
        return current_fib    
    
main()    