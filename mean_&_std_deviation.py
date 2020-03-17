"""
Neha Bais
MET CS-521 A3

Assignment 10.9

Input numbers from user and
Calculate mean and standard deviation

"""

def mean(x) :
    n = len(x)
    total = 0
    for e in x :
        total = total + e
    
    # Calculating mean and formatting it to 2 decimal places
    mean = float('%.2f'  %(total / n))
    
    return mean
    
def deviation(x,y) :
    import math
    n = len(x)
    total = 0
    for e in x :
        total = total + (e - y)**2
     
    # Calculating deviation and formatting it to 5 decimal places    
    deviation = float('%.5f' %( math.sqrt(total / (n - 1) )))
    
    return deviation
        
        
def main() :

    user_nbr = input('Enter numbers separated by spaces : ')
    
    # Convert string to list
    nbr_list = user_nbr.split()
    
    # Convert elements in list to float
    x = [float(e) for e in nbr_list]
    
    y = mean(x) 
    print('The mean is : ', y)
    
    z = deviation(x,y)
    print('The deviation is : ' , z) 
    
main()     