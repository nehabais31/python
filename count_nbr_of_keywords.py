"""
Neha Bais

(Display keywords) Revise Listing 14.4 CountKeywords.py to display the keywords
in a Python source file as well as to count the number of the keywords.

"""

import os.path
import sys

def main() :
    keywords = {
        "and", "as", "assert", "break", "class",
        "continue", "def", "del", "elif", "else",
        "except", "False", "finally", "for", "from",
        "global", "if", "import", "in", "is", "lambda",
        "None", "nonlocal", "not", "or", "pass", "raise",
        "return", "True", "try", "while", "with", "yield" }
     
   
    filename = input("Enter a python source code filename : ").strip()
    
    path = os.path.join('E:\\','Neha','Spring 2020','CS521 Python',filename)
    
    # Check if file exists
    if not os.path.isfile(path) :
        print("File", filename, "does not exist")
        sys.exit()
        
    infile = open(path,'r')
    
    text = infile.read().split()
    
    # Empty set to capture the keywords in file
    file_keywords = set()
    
    count = 0
    
    # Checking for keywords in file
    for word in text :
        if word in keywords :
            count += 1
            file_keywords.add(word)        # add a keyword in set if exists in file
            
    print("The number of keywords in file : " , count)
    print("The list of keywords in file : \n", file_keywords)
        
main()    
