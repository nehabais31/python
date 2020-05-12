'''
Neha Bais
MET CS-521 A3

String editor functions and cursor movements

for cmd_wq: Output file is saved at the mentioned location

Functions of my choice:
1. cmd_dw   : Delete the entire word to the right of cursor & cursor at start of next word
2. cmd_case : Change the case of character at the cursor position
3. cmd_f    : Move cursor to the start of next word
4. cmd_b    : Move cursor to the start of previous word
5. cmd_J    : Merge current line and next line, cursor at start of next line    

'''

x_str="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""


x_list = list(x_str)
cursor = 4

def print_file(x_str, cursor, sep='^'):
    print( x_str[0:cursor] + sep + x_str[cursor : ] + '\n')
    
def cmd_h(x_str, cursor, sep='^'):     # move left one position
    print('-----Move Cursor left one position-----')
    if cursor > 0:
        cursor = cursor - 1
    return(x_str, cursor)    
    
def cmd_l(x_str, cursor, sep='^'):     # move right one position
    print('-----Move cursor right one position-----')
    if cursor < len(x_str) - 1:
        cursor = cursor + 1
    return(x_str, cursor)  
    
def cmd_start_line(x_str, cursor):     # find start of line
    pos = x_str.rfind('\n', 0, cursor)
    if pos > 0:
        return pos + 1
    else:
        return 0
        
def cmd_end_line(x_str, cursor):      # find end of line
    pos = x_str.find('\n', cursor)
    if pos >= 0:
        return pos + 1
    else :
        return len(x_str)
        
def cmd_j(x_str, cursor):             # move vertically down one line
    print('-----Move cursor vertically down one line-----')
    a = cmd_start_line(x_str, cursor)
    delta = cursor - a
    b = cmd_end_line(x_str, cursor)
    if b < len(x_str):
        cursor = b + delta
    return(x_str, cursor) 
    
def cmd_k(x_str, cursor):           #  move vertically up one line  
    print('-----Move cursor vertically up one line-----')
    a = cmd_start_line(x_str, cursor)
    if a > 0:
        b = cmd_start_line(x_str, a -1)
    delta  = cursor - a
    cursor = b + delta
    return(x_str, cursor)   
        
def cmd_X(x_str, cursor):            # delete 1 char to left of cursor
    print('-----Delete 1 char to left of cursor-----')
    if cursor > 0:
        left_part  = x_str[0 : cursor - 1]
        right_part = x_str[cursor : ]
        x_str = left_part + right_part
        return x_str,cursor-1
    else:
        return x_str, cursor    
    
def cmd_D(x_str, cursor):           # remove on current line from cursor to the end
    print('-----Delete from cursor to end of current line-----')
    if cursor >= 0:
        left_part = x_str[0 : cursor]
        b = cmd_end_line(x_str, cursor)
        right_part = x_str[b : len(x_str)]
        x_str = left_part + '\n' + right_part
        return x_str,cursor
    else :
        return x_str, cursor
    
def cmd_dd(x_str, cursor):          # del current line, cursor -> start of next line
    print('-----Del current line & place cursor to start of next line-----')
    if cursor >= 0:
        a = cmd_start_line(x_str, cursor)
        left_part = x_str[0 : a]
        b = cmd_end_line(x_str, cursor)
        right_part = x_str[b : len(x_str)]
        cursor = a
        x_str = left_part  + right_part
        return x_str,cursor
    else :
        return x_str, cursor 
        
def cmd_ddp(x_str, cursor):         # transpose 2 adjacent lines 
    print('-----Transpose 2 adjacent lines-----')
    a = cmd_start_line(x_str, cursor)
    delta = cursor - a
    b = cmd_end_line(x_str, cursor)
    if b < len(x_str):
        c = cmd_end_line(x_str, b)
    part_1 = x_str[0 : a]
    part_2 = x_str[a : b]
    part_3 = x_str[b : c]
    part_4 = x_str[c :  ]
    x_str  = part_1 + part_3 + part_2 + part_4
    cursor = len(part_1) + len(part_3) + delta
    return(x_str, cursor)
    
def cmd_n(x_str, cursor, target):              # next occurence of target
    print('-----Find next occurrence of target-----')
    pos = x_str.find(target, cursor)
    if pos >= 0:
        return x_str, pos
    else :
        return x_str, cursor
    
def cmd_wq(x_str, cursor):                    # write in text file and save it   
    print('-----Writing the representation in text file-----')
    import os.path
    file_name = 'string_editor.txt'
    file_path = r'E:\Neha\Spring 2020\CS521 Python\Assignment 7\{}'.format(file_name)
    if os.path.isfile(file_path):
        print('File already exists')
    else :
        file_out = open(file_path , 'w')
        data = x_str[0:cursor] + '^' + x_str[cursor : ] + '\n'
        file_out.write(data)
        file_out.close()    
        
def cmd_dw(x_str, cursor):
    print('-----Delete the entire word from the cursor position to right-----')
    pos = x_str.find(' ', cursor)
    if pos < len(x_str):
        left_part  = x_str[0:cursor]
        right_part = x_str[pos + 1:len(x_str)]
        x_str = left_part + right_part
        return x_str, cursor
    else :
        return x_str, cursor
    
def cmd_case(x_str, cursor):      # change the case of character to right of cursor
    print('-----Change case of char at the cursor position-----')
    ch    = x_str[cursor]
    if ch.isalpha() :
        delta = ord('a') - ord('A')
        if ord(ch) < ord('a'):
            change_case = ord(ch) + delta
        else :
            change_case = ord(ch) - delta
    
        x_str = x_str[0:cursor] + chr(change_case) + x_str[cursor+1 : ]
        return x_str, cursor
    else:
        return(x_str, cursor)  
        
def cmd_f(x_str, cursor):                   # shift cursor at the start of next word
    print('-----Move the cursor one word forward-----')
    pos = x_str.find(' ' , cursor)
    if pos < 0 :
        return x_str, cursor
    else :
        return x_str , pos + 1    

def cmd_b(x_str, cursor):                   #shift cursor at the start of previous word
    print('-----Move the cursor one word backward-----')
    pos_1 = x_str.rfind(' ' ,0, cursor)
    if pos_1 > 0 :
        pos_2 = x_str.rfind(' ' , 0 , pos_1)
        if pos_2 < 0 :
            return x_str, cursor
        else :
            return x_str , pos_2 + 1
    else :
        return x_str,cursor
    
def cmd_J(x_str , cursor):               # merge current and next line & cursor at start of next line
    print('-----Merge current line and next line-----')
    a = cmd_end_line(x_str, cursor)
    if a < len(x_str) :
        b = cmd_end_line(x_str, a)
        part_1 = x_str[0 : a -1]
        part_2 = x_str[a : b -1]
        part_3 = x_str[b - 1 : ]
        x_str = part_1 + part_2 + part_3
        return x_str , a-1
    else :
        return x_str, cursor     # do nothing when cursor is at last line
           

print('-----Initial string-----')
print_file(x_str,cursor) 

x_str, cursor  = cmd_h(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_l(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_j(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_k(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_X(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_D(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_dd(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_ddp(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_n(x_str, cursor, 'better')
print_file(x_str, cursor)

write_file = cmd_wq(x_str, cursor)
print('File Saved!!! \n')

x_str, cursor = cmd_dw(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_case(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_f(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_b(x_str, cursor)
print_file(x_str, cursor)

x_str, cursor = cmd_J(x_str, cursor)
print_file(x_str, cursor)