"""
Created on Sat Mar 28 13:05:23 2020

@author: Neha Bais
Assignment 9

Printing file with cursor movements using
Double Linked List

Output text file saved: double_list_editor.txt

"""

x_str="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated."""

x_list = x_str.split('\n')

DATA = 0
NEXT_PTR = 1
PREV_PTR = 2
  

def print_file_double_list(head, tail, node, delta):
    result = ''
    next_node = head
    while next_node is not None:
        if node == next_node:
            curr_line = node[DATA]
            curr_line = curr_line[ : delta] + '^' + curr_line[delta : ]
            result = result + '\n' + curr_line 
        else:
             result = result + '\n' + next_node[DATA]
        next_node = next_node[NEXT_PTR]   
    print(result)
    return

# Construct  Double Link List 
def construct_double_list(x) :
    head = None
    tail = None
    for e in x :
        new_node = [e, None, None]
        if head is None:
            head = new_node
            tail = new_node
        else :
            tail[NEXT_PTR] = new_node
            new_node[PREV_PTR] = tail
            tail = new_node
    return head, tail

# Move cursor 1 position left
def cmd_h_double_list(head, tail, node, delta):
    if node is None:
        return head, tail, node, delta    
    else :
        if node != head :
            if delta > 0 :
                delta = delta - 1
            else :
                node = node[PREV_PTR]
                delta = len(node[DATA])-1
        else :
            if delta > 0:
                delta = delta - 1
        return head, tail, node, delta

# Move cursor 1 position right
def cmd_l_double_list(head, tail, node, delta):
    if node is None:
        return head, tail, node, delta
    else :    
        if node != tail :
            if delta < len(node[DATA])-1 :
                delta = delta + 1
            else :
                node = node[NEXT_PTR]
                delta = 0
        else :
            if delta < len(node[DATA])-1:
                delta = delta + 1
        return head, tail, node, delta 

# Transpose 2 adjacent lines       
def cmd_ddp_double_list(head, tail, node, delta):
    if node is None:
        return head, tail, node, delta
    else :
        p_node = node[PREV_PTR]
        n_node = node[NEXT_PTR]
        if p_node is None:      # current node is head
            # next_node link 
            new_head = n_node
            temp = n_node[NEXT_PTR]
            new_head[NEXT_PTR] = node
            new_head[PREV_PTR] = None
            
            # current node link
            node[PREV_PTR] = new_head
            node[NEXT_PTR] = temp
            return new_head, tail, node, delta
        
        else :
            if n_node == tail : # next_node is tail
                new_tail = node
                tail[NEXT_PTR] = node
                tail[PREV_PTR] = p_node
                new_tail[PREV_PTR] = tail
                new_tail[NEXT_PTR] = None
                p_node[NEXT_PTR] = tail
                return head, new_tail, node, delta
            
            else :
                if n_node is not None:       # next node is not tail
                    # previous node link updation
                    p_node[NEXT_PTR] = node[NEXT_PTR]
                
                    # next node link updation
                    temp = n_node[NEXT_PTR]
                    n_node[NEXT_PTR] = node
                    n_node[PREV_PTR] = node[PREV_PTR]
            
                    # current node link updation
                    node[PREV_PTR] = node[NEXT_PTR]
                    node[NEXT_PTR] = temp
    
    return head, tail, node, delta  


# Remove text from cursor to the end of current line
def cmd_D_double_list(head, tail, node, delta):
    if node is None:
        return head, tail, node, delta
    else :    
        curr_line = node[DATA]
        curr_line = curr_line[ : delta]
        node[DATA] = curr_line
        return head, tail, node, delta

# Delete current line
def cmd_dd_double_list(head, tail, node, delta):
    if node is None:
        return head, tail, node, delta
    else :
        p_node = node[PREV_PTR]
        n_node = node[NEXT_PTR]
        if p_node is None:
            new_head = head[NEXT_PTR]
            new_head[PREV_PTR] = None
            return new_head, tail, new_head, 0
        elif n_node is None:
            new_tail = tail[PREV_PTR]
            new_tail[NEXT_PTR] = None
            return head, new_tail, new_tail, 0
        else:
            p_node[NEXT_PTR] = n_node
            n_node[PREV_PTR] = p_node
            return head, tail, n_node, 0  

# Writing the file representation in text file
def cmd_wq_double_list(head, tail):
    file_name = r'E:\Neha\Spring 2020\CS521 Python\Assignment 9 Linked List\double.txt'
    text_file = open(file_name , 'w') 
    next_node = head
    while next_node is not None :
        text_file.writelines(next_node[DATA] + '\n')
        next_node = next_node[NEXT_PTR]
    text_file.close()

# Construct Double linked list
head , tail = construct_double_list(x_list)

curr_node = head
delta = 4


print('-----Initial File-----')
print_file_double_list(head, tail, curr_node, delta)

print('\n-----Writing file representation in text file-----')
cmd_wq_double_list(head, tail)
print('File Saved!!!')

head, tail, node, delta = cmd_h_double_list(head, tail, curr_node, delta)
print('\n-----Moving cursor left 1 position-----')
print_file_double_list(head, tail, curr_node, delta)

head, tail, node, delta = cmd_l_double_list(head, tail, curr_node, delta)
print('\n-----Moving cursor right 1 position-----')
print_file_double_list(head, tail, curr_node, delta)

head, tail, curr_node, delta = cmd_ddp_double_list(head, tail, curr_node, delta)
print('\n-----Transpose current and next line-----')
print_file_double_list(head, tail, curr_node, delta)

head, tail, curr_node, delta = cmd_D_double_list(head, tail, curr_node, delta)
print('\n-----Remove text from cursor to end of line-----')
print_file_double_list(head, tail, curr_node, delta)

head, tail, curr_node, delta = cmd_dd_double_list(head, tail, curr_node, delta)
print('\n-----Delete current line-----')
print_file_double_list(head, tail, curr_node, delta)

