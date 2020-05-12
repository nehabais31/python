"""
finds the number of
times the fib function is called in below
fibonacci recursive function call

@author: Neha Bais
MET CS-521 A3
"""


index = eval(input('Enter an index for Fibonacci number: '))
count = 0 
    
def fib(index):
    '''
    Recursive function to generate
    fibonacci number of input index
    '''
    global count          # global variable
    
    # increment counter to check for number of function call
    count += 1             
    
    if index == 0:
        return 0          # base case
    elif index == 1:
        return 1          # base case
    else:
        return fib(index - 1) + fib(index - 2)
        

    
print("Fibonacci number at index", index , "is: " , fib(index) )
print("fib function is called", count, "times")
         
    