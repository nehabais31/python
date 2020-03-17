"""
Neha Bais

Write a program that prompts the user to enter an integer
from 1 to 15 and displays a pyramid, as shown in the following sample run:
Enter the number of lines:
            1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
  6 5 4 3 2 1 2 3 4 5 6
7 6 5 4 3 2 1 2 3 4 5 6 7
"""

def main() :
    
    num = eval(input("Enter an integer from 1 to 15: ")) 
    
    if num >= 1 and num <= 15 :
        pyramid = ""   # Empty string 
    
    
        for j in range(1,num+2):

            # capture leading spaces                                                                                                                                 
            row = " "*3*(num-j+1)

            # reverse string                                                                                                                                       
            for i in range(j-1,1,-1):
                if i < 10 :
                    s = ' '
                else :
                    s = ''
                row = row + s + str(i) + " "

            # forward string                                                                                                                                        
            for i in range(1,j):
                s = str(i)
                if i < 10 :
                    s = ' '
                else :
                    s = ''
                row = row + s + str(i) + " "

            row = row + "\n"
            pyramid = pyramid + row

        print (pyramid)
    else :
        print('Number is not in specified range')

main()