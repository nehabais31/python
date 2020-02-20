"""
Print distinct numbers) Write a program that reads in numbers separated by a
space in one line and displays distinct numbers (i.e., if a number appears multiple
times, it is displayed only once). (Hint: Read all the numbers and store
them in list1. Create a new list list2. Add a number in list1 to list2.
If the number is already in the list, ignore it.)

"""

def distinct_list(list1) :
     
    #Empty list
    list2 = []

    #Check empty list for the elements of input list , append if not exists
    for e in list1 :
        if e not in list2 :
            list2.append(e)
        
    print ("The distinct numbers are : " , list2)


def main() :
    x = input("Enter 10 numbers separated by spaces : ")
    x_split = x.split()    

    #converting strings of list to integers
    list1 = [eval(e) for e in x_split]  
    distinct_list(list1)
    
main()    