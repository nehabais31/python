"""
Neha Bais
MET CS-521 A3

List editor functions and cursor movements

for cmd_wq: Output file is saved at the mentioned location 
(attached output file as well)

Functions of my choice:
1. cmd_dw   : Delete the entire word to the right of cursor & cursor at start of next word
2. cmd_case : Change the case of character at the cursor position
3. cmd_f    : Move cursor to the start of next word
4. cmd_b    : Move cursor to the start of previous word
5. cmd_J    : Merge current line and next line, cursor at start of next line 

"""

x_str="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

x_list = x_str.split('\n')

line_id = 3
delta = 3

def print_list(x, line_id, delta) :
    left_list  = x[0 : line_id]
    left_str   = '\n'.join(left_list)
    right_list = x[line_id + 1 : ]
    right_str  = '\n'.join(right_list)
    curr_line  = x[line_id]
    ready_line = curr_line[0 : delta] + '^' + curr_line[delta : ]
    temp_list  = [left_str , ready_line , right_str]
    print('\n'.join(temp_list) + '\n')
    

# Move cursor left 1 position    
def cmd_h_list(x, line_id, delta) :
    if line_id > 0 :
        if delta > 0:
            delta = delta -1 
        else :
            line_id = line_id - 1
            delta   = len(x[line_id])
    else :
        if delta > 0:
            delta = delta - 1
    return x, line_id, delta    
 
# Move cursor right 1 position    
def cmd_l_list(x, line_id, delta):
    if line_id < len(x)-1 :
        if delta < len(x[line_id])-1 :
            delta = delta + 1
        else :
            line_id = line_id + 1
            delta   = 0
        return x, line_id, delta
    else :
        if delta < len(x[line_id])-1 :
            delta = delta + 1
        return x, line_id, delta   

# Move cursor vertically down
def cmd_j_list(x, line_id, delta):
    if line_id < len(x)-1 :
        next_line = x[line_id + 1] 
        if delta > len(next_line) :
            return x, line_id + 1, len(next_line)-1
        else :
            return x, line_id+1 , delta
    else :      
        return x, line_id, delta 

# Move cursor vertically up 
def cmd_k_list(x, line_id, delta):
    if line_id > 0 :
        prev_line = x[line_id - 1] 
        if delta > len(prev_line) :
            return x, line_id - 1, len(prev_line)-1
        else :
            return x, line_id-1 , delta
    else :      
        return x, line_id, delta

# Delete char to the left of cursor
def cmd_X_list(x, line_id, delta):
    if delta > 0 :
        curr_line  = x[line_id]
        left_part  = curr_line[0 : delta-1]
        right_part = curr_line[delta : ]
        x[line_id] = left_part + right_part
        return x, line_id, delta-1
    else :
        return x, line_id, delta  

# Delete current line from cursor to end of current line 
def cmd_D_list(x, line_id, delta):
    curr_line = x[line_id]
    left_part = curr_line[ : delta]
    x[line_id] = left_part
    return x, line_id, delta  

# Delete  current line & cursor at start of next line
def cmd_dd_list(x, line_id, delta):
    if line_id < len(x) - 1 :
        x.pop(line_id)
        delta = 0
        return x, line_id, delta 
    else :
        return x, line_id, delta

# Transpose two adjacent lines
def cmd_ddp_list(x, line_id, delta):
    if line_id < len(x) - 1 :
        curr_line      = x[line_id]
        next_line      = x[line_id + 1]
        x[line_id]     = next_line
        x[line_id + 1] = curr_line
        line_id = line_id + 1
        return x, line_id, delta
    else :
        return x, line_id, delta   

# Search for next occurence of target
def cmd_n_list(x, line_id, delta, target):
    curr_line = x[line_id]
    pos = curr_line.find(target, delta)
    if pos < 0 :
        for i in range(line_id+1 , len(x)) :
            curr_line = x[i]
            next_pos  = curr_line.find(target, 0)
            if next_pos >= 0 :
                line_id = i
                delta   = next_pos
                return x, line_id, delta
        return x, line_id, delta        
    else :
        delta = pos
        return x, line_id, delta 
    
    
# Writing the representation to a file
def cmd_wq(x):
    file_name = 'E:\\Neha\\Spring 2020\\CS521 Python\\Assignment 8\\list_editor.txt'
    text_file = open(file_name, 'w')
    text_file.writelines('%s\n' %list_item for list_item in x)
    text_file.close()  
    print('-----File written and saved!!!-----\n')  
    
 
# Delete the word starting from cursor position    
def cmd_dw_list(x, line_id, delta):
    curr_line = x[line_id]
    pos = curr_line.find(' ', delta)
    left_part  = curr_line[0 : delta]
    right_part = curr_line[pos : ]
    x[line_id] = left_part + right_part
    if pos > 0 :
        delta = delta + 1
        return x, line_id, delta
    else :
        return x, line_id, delta  
    
# Chnge the case of character at the cursor position      
def cmd_case_list(x, line_id, delta):
    curr_line = x[line_id]
    if delta < len(curr_line):
        ch = curr_line[delta]
        if ch.isalpha() :
            case_ord_diff = ord('a') - ord('A')
            if ord(ch) < ord('a'):
                change_case = ord(ch) + case_ord_diff
            else :
                change_case = ord(ch) - case_ord_diff
        
            x[line_id] = curr_line[ : delta] + chr(change_case) + curr_line[delta+1 : ]
            return x, line_id, delta
        else :
            return x, line_id, delta 
    return x, line_id, delta 

# Move cursor one word forward
def cmd_f_list(x, line_id, delta):
    curr_line = x[line_id]
    pos = curr_line.find(' ' , delta)
    if pos > 0:
        delta = pos + 1
        return x, line_id, delta
    else :
        if line_id < len(x)-1 :
            return x, line_id+1, 0
    return x, line_id, delta   

# Move cursor one word backward
def cmd_b_list(x, line_id, delta):
    curr_line = x[line_id]
    pos_1 = curr_line.rfind(' ' , 0 , delta)
    if pos_1 > 0 :
        if curr_line[delta] == ' ' :
            delta = pos_1 + 1
            return x, line_id, delta
        else :
            pos_2 = curr_line.rfind(' ', 0 ,pos_1)
            if pos_2 > 0 :
                delta = pos_2 + 1
                return x, line_id, delta
            else :
                delta = 0
                return x, line_id, delta
    else :
        if line_id > 0 :
            line_id = line_id -1 
            curr_line = x[line_id]
            pos_3 = curr_line.rfind(' ',0 , len(curr_line))
            delta = pos_3 + 1
            return x, line_id, delta
        else :
            return x, line_id, delta
        
# Merge current line and next line & cursor at the start of line that is merged
def cmd_J_list(x, line_id, delta):    
    if line_id < len(x)-1 :
        curr_line = x[line_id]
        next_line = x[line_id + 1]
        new_curr_line = [curr_line + next_line]
        part_1 = x[0 : line_id]
        part_2 = new_curr_line
        part_3 = x[line_id+2 : ]
        x = part_1 + part_2 + part_3
        delta = len(curr_line)
        return x, line_id, delta
    else :
        return x, line_id, delta        
    
     
    
print('-----Initial string-----')   
print_list(x_list, line_id, delta)    

write_file = cmd_wq(x_list)

print('-----Move cursor left 1 position-----')
x_list, line_id, delta = cmd_h_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Move cursor right 1 position-----')
x_list, line_id, delta = cmd_l_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Move cursor vertically down-----')
x_list, line_id, delta = cmd_j_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Move cursor vertically up-----')
x_list, line_id, delta = cmd_k_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Del char to left of cursor-----')
x_list, line_id, delta = cmd_X_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Del from current line cursor to the end-----')
x_list, line_id, delta = cmd_D_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Del current line & cursor to the start of next line-----')
x_list, line_id, delta = cmd_dd_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Transpose two adjacent lines-----')
x_list, line_id, delta = cmd_ddp_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Search next occurence of target-----')
x_list, line_id, delta = cmd_n_list(x_list, line_id, delta, 'better')
print_list(x_list, line_id, delta)

print('-----Delete entire word from cursor position to right-----')
x_list, line_id, delta = cmd_dw_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Change the case of character at the delta position-----')
x_list, line_id, delta = cmd_case_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Move cursor at the start of next word-----')
x_list, line_id, delta = cmd_f_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Move cursor at the start of previous word-----')
x_list, line_id, delta = cmd_b_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)

print('-----Merge current line and next line & cursor at the start of next line that is merged-----')
x_list, line_id, delta = cmd_J_list(x_list, line_id, delta)
print_list(x_list, line_id, delta)





