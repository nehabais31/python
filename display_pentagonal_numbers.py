"""
Created on Wed Apr  1 17:05:36 2020

@author: Neha Bais
MET CS-521 A3

Print first 100 pentagonal numbers with 10 numbers on each line.

"""

def getPentagonalNumber(n, count) :
    '''
    First 100 pentagonal numbers
    with 10 numbers on each line
    
    '''
    for e in n :
        x = (e * (3 * e - 1)) // 2
        count = count + 1
        if count <= 10 :
            print(x , end = ' ')
        else :
            print()
            print(x , end = ' ')
            count = 1

n = []       # Empty list to store first 100 integers
for i in range (1, 101) :
    n.append(i)

# Calling function to get the first 100 pentagonal numbers
print(getPentagonalNumber.__doc__)    
getPentagonalNumber(n,  0) 
   