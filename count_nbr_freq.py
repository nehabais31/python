"""
Neha Bais
MET CS-521 Spring'20

Assignment 10.3
reads some integers
between 1 and 100 and counts the occurrences of each.

"""

def num_dict(num) :
    # Empty dictionary 
    num_dict = {}

    # Count of numbers in list
    for i in num :
        if i in num_dict :
            num_dict[i] += 1
        else :
            num_dict[i] = 1
        
    # Scanning dictionary to print output
    for e in num_dict :
        if num_dict[e] > 1 :
            print (e, "occurs" , num_dict[e] , "times.")
        else :
            print (e, "occurs" , num_dict[e] , "time.")
            
            
def main() :
    
    num_inp = input("Enter integers between 1 and 100 : ")

    # Creating List from the values entered
    num_list = num_inp.split()      

    # Converting string to integers
    x  = [eval(e) for e in num_list] 

    # Empty list 
    num = []

    # Range check (1 and 100 ) and store in empty list if True
    for e in x : 
        if e >= 1 and e <= 100 :
            num.append(e)

    num_dict(num)        
        
main()