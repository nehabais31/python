"""
Neha Bais

Printing a pyramid pattern
for nbr_of rows = 8
                              1 
                         1    2    1 
                         1    2    4    2    1 
                    1    2    4    8    4    2    1 
               1    2    4    8   16    8    4    2    1 
          1    2    4    8   16   32   16    8    4    2    1 
     1    2    4    8   16   32   64   32   16    8    4    2    1 
1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 

"""

# number of rows 
num = 8

for row in range(num) :
    # printing spaces
    for col in range(0, num-row) :
        print('%4c' %' ' , end = ' ')           # padding for alignment
    
    # printing left pyramid
    i = 0
    for col in range(row , -1 , -1) :
        print('%4d' %(2**i) , end = ' ')        # padding for alignment
        i = i + 1
     
    # printing right pyramid    
    for col in range(row-1 , -1 , -1) :
        print('%4d' %(2**col) , end = ' ')      # padding for alignment
    print()    