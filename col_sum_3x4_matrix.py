"""
Neha Bais
MET CS-521 Spring'20

(Sum elements column by column) Write a function that returns the sum of all the
elements in a specified column in a matrix using the following header:
def sumColumn(m, columnIndex):
Write a test program that reads a matrix and displays the sum of each column.

"""

def get_matrix() :
    
    # Empty list
    matrix = []         
    
    for rows in range(3) :    
        x = input("Enter a 3-by-4 matrix row for row " +str(rows) + ": ")
        x = x.split()
        value = [float(e) for e in x]       # Converting string to float in list x
        matrix.append(value)
    
    return (matrix)  
    
        
def sumColumn(m,columnIndex) :
    
    total = 0.0
    for row in range(len(m)) :
        total += m[row][columnIndex]
    print("Sum for column " ,columnIndex , "is : " , total)    
        
              
def main() :
    
    # Create a matrix
    m = get_matrix()         
      
    for columnIndex in range (len(m[0])) :
        sumColumn(m , columnIndex)          # Calculate sum of each columns
        
main()  