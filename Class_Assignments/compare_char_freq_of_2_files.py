"""
Neha Bais

Read 2 txt files, analyse and compare
freq distribution of each letter.

Source Files used :
File_1 : White Fang.txt
File_2 : A Farewell To Arms.txt

Place the file at mentioned path 

"""

def first_file_routine(first_path) :
    
    # dict to store keys a to z with initial count 0
    freq_dict_1 = dict( (chr(key) , 0) for key in range(ord('a') ,ord('z') + 1) )
    
    # list to store all the characters of the file
    characters  = []
    
    inp_file_1    =  open(first_path , 'r')
    
    for line in inp_file_1 :
        words    = line.split(' ')       # line into words
        
        for word in words :
            char = list(word)            # words into characters
            characters.append(char)      # list of characters 
        
    for i in characters :
        for ch in i :
            if ch.isalpha() :        # alphabet check
                ch = ch.lower()      # coverting to lower case
                    
                if ch in  freq_dict_1.keys() :
                    current_count = freq_dict_1[ch]
                    current_count = current_count + 1
                    freq_dict_1[ch] = current_count
                      
    char_count_1 = sum(freq_dict_1.values())      # total count of all the characters          
    return(freq_dict_1 , char_count_1)
        
    inp_file_1.close()
    
    
    
def second_file_routine(second_path) :
 
    # dict to store keys a to z with initial count 0    
    freq_dict_2 = dict( (chr(key) , 0) for key in range(ord('a') ,ord('z') + 1) )
    
    # list to store each character of file
    characters  = []
    
    inp_file_2    =  open(second_path , 'r')
    
    for line in inp_file_2 :
        words    = line.split(' ')         # line to words
        
        for word in words :
            char = list(word)              # word to list
            characters.append(char)        # list of characters
    
    for i in characters :
        for ch in i :
            if ch.isalpha() :          # alphabet check
                ch = ch.lower()        # converting to lower case
                    
                if ch  in  freq_dict_2.keys() :
                    current_count = freq_dict_2[ch]
                    current_count = current_count + 1
                    freq_dict_2[ch] = current_count
                       
    char_count_2 = sum(freq_dict_2.values())     # total count of characters in file               
    return(freq_dict_2 , char_count_2)                   
        
    inp_file_2.close()

    

    
def main() :
    import os.path
    
    first_file  = input('Enter the first filename: ')
    second_file = input('Enter the second filename: ')

    first_path  = r'E:\Neha\Spring 2020\CS521 Python\Assignment6\Source_Files\{}'.format(first_file)
    second_path = r'E:\Neha\Spring 2020\CS521 Python\Assignment6\Source_Files\{}'.format(second_file)

    # read first file and store character count in first_dict 
    if os.path.isfile(first_path):
        first_dict, char_count_1 = first_file_routine(first_path)
    else :
        print('File', first_file , 'does not exist.')

    # read second file and store character count in second_dict
    if os.path.isfile(second_path):
        second_dict , char_count_2 = second_file_routine(second_path) 
    else :
        print('File', second_file , 'does not exist.')


    # printing routine
    print('Letter' , '\t\t' , 'Book_1' , '\t\t' , 'Book_2')
    
    for i in first_dict :
        for j in second_dict :
            if i == j:
               freq_count_1 = (first_dict[i] / char_count_1) * 100 
               freq_count_2 = (second_dict[j] / char_count_2) * 100
               print(i , '\t\t' , '%4.1f' %(freq_count_1),'%' ,'\t\t' , '%4.1f' %(freq_count_2),'%')

            
main()