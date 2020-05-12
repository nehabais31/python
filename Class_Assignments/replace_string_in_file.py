"""
Neha Bais


Input  : Prompt user to enter file name , old & new string 
Output : Replace the old string with new string in the file

Pre-Requisite :
Input File : test.txt   (attached in src_file zip folder)

- Place the file at the file_path mentioned in code.
- Enter old_string = happy 
- Enter new_string = sad
- Run the code and check the file for replaced string

"""

import os.path

file_name  = input('Enter a filename: ' )

old_string = input('Enter the old string to be replaced: ')
new_string = input('Enter the new string to replace the old string: ')

file_path = r'E:\Neha\Spring 2020\CS521 Python\Source_Files\{}'.format(file_name)

if os.path.isfile(file_path) :
    inp_file  = open(file_path,'r')              # open file in read mode
    old_data  = inp_file.read()                  # read entire data 
      
    # replace old string with new string
    new_data  = old_data.replace(old_string , new_string)

    inp_file.close()                            # close file
    
    inp_file  = open(file_path , 'w')           # open file in write mode
    inp_file.write(new_data)                    # write new data having replacement in file
    inp_file.close()                            # close file
    
    print('Done')
    
else : 
    print('File not found.') 
       
   