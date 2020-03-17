# -*- coding: utf-8 -*-
"""
Neha Bais
(Display a pattern) Write a program that displays the following pattern:
    
FFFFFFF U    U NN    NN
FF      U    U NNN   NN
FFFFFFF U    U NN N  NN
FF      U    U NN  N NN
FF       UUU   NN   NNN

"""


# Creating 3 empty string list for 3 characters

list_F = [[" " for i in range(7)] for j in range(5)]
list_U = [[" " for i in range(7)] for j in range(5)]
list_N = [[" " for i in range(8)] for j in range(5)]

# For pattern F

for row in range (5):
    for col in range (7):
        if (col == 0 or col == 1) or \
           ((row == 0 or row == 2) and col > 0) :
            list_F[row][col] = "F"
            
# FOr Pattern U

for row in range (5):
    for col in range (7):
        if (((col == 0 or col == 6) and row < 3) or \
        ((col == 1 or col == 5) and row == 3) or  \
        ((col > 1 and col < 5) and row == 4)) : 
            list_U[row][col] = "U"
            
# for pattern N

for row in range (5):
    for col in range (8):
        if ((col < 2 or col > 5) or 
        (col == 2 and row == 1) or
        (col == 3 and row == 2) or
        (col == 4 and row == 3) or
        (col == 5 and row == 4)) :
            list_N[row][col] = "N"
            
# Printing the characters stored in the lists        

for i in range(5) :
    for j in range(7) :
        print (list_F[i][j] , end = "")
    print (end = "  ")   
    for j in range(7) :
        print (list_U[i][j] , end = "")
    print (end = "  ")   
    for j in range(8) :
        print (list_N[i][j] , end = "")
    print (end = "  ")    
    print()    