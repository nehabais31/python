"""
Neha Bais

Write a program that reads the scores from the file 
and displays their total and average. 
Scores are separated by blanks

Pre-Requisite :
Input-File : scores.txt (attached in src_files folder)
Place the file at the mentioned path.
Run the code.

"""

def compute_total_average(scores) :
    total   = 0
    average = 0
    
    for e in scores :
        total = total + e
    
    average       = total / len(scores)
    return(total , average)
    
def main() :
    import os.path    

    file_name = input('Enter the File name: ')

    file_path = r'E:\Neha\Spring 2020\CS521 Python\Source_Files\{}'.format(file_name)

    # check for file existence
    if os.path.isfile(file_path) :
        inp_file   =  open(file_path,'r')                    # open file in read mode
        data        =  inp_file.read()                       # read entire data
        scores      =  [eval(e) for e in data.split() ]      # store the scores in a list
    
        # function call to calculate total and average
        total , average = compute_total_average(scores)
               
        nbr_of_scores   = len(scores)
        
        inp_file.close()                                    # close the file 
        
        print('There are' , nbr_of_scores , 'scores')
        print('The Total is: ', total)
        print('The Average is: ' , average)
    
    else :
        print('File not present.')    
        
main()        