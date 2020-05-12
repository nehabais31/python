"""
Input : Prompts user to enter file name and string to be removed
Output : Removes the string from all occurences in the file.

"""

import os.path

inp_file = input ("Enter a file name :")
str_to_remove = input ("Enter the string to be removed: ")

file_path = r'E:\Neha\Spring 2020\CS521 Python\Source_Files\{}'.format(inp_file)

if os.path.isfile(file_path) :                           # Error handling
    file_in = open(file_path,"r")                  # Open and read the input file
    data = file_in.read()                          # read entire data in data variable
    data = data.replace(str_to_remove,'') 
    file_in.close()

# Open and write the updated string in inp_file    
    file_in = open(file_path,'w')
    file_in.write(data)                           # write the string stored in variable data to the file
    file_in.close()

    print("Done.")
else :
    print("File not found")    


       