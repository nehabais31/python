# -*- coding: utf-8 -*-
"""
Neha Bais

Write a program that prompts the user to
enter the month and year and displays the number of days in the month. For example,
if the user entered month 2 and year 2000, the program should display that
February 2000 has 29 days. If the user entered month 3 and year 2005, the program
should display that March 2005 has 31 days.

"""

def main() :

    inp_month , inp_year = eval(input("Enter a month and year separated by comma : "))
    
    check_for_days(inp_month,inp_year)
    

def check_for_days(inp_month,inp_year) :
    
    #check for invalid month
    if inp_month < 1 or inp_month > 12 :
        print("Invalid month.")
        
    # check for days for month 
    if inp_month == 2 :
        if ((inp_year % 4 == 0 and inp_year % 100 != 0) or \
            inp_year % 400 == 0) :
            print("February" , inp_year , "has 29 days.")
        else :
            print("February" , inp_year , "has 28 days.")
    elif inp_month == 1 :
        print("January" , inp_year , "has 31 days.")
    elif inp_month == 3 :
        print("March" , inp_year , "has 31 days.")
    elif inp_month == 4 :
        print("April" , inp_year , "has 30 days.")
    elif inp_month == 5 :
        print("May" , inp_year , "has 31 days.")
    elif inp_month == 6 :
        print("June" , inp_year , "has 30 days.")
    elif inp_month == 7 :
        print("July" , inp_year , "has 31 days.")
    elif inp_month == 8 :
        print("August" , inp_year , "has 31 days.")
    elif inp_month == 9 :
        print("September" , inp_year , "has 30 days.")
    elif inp_month == 10 :
        print("October" , inp_year , "has 31 days.")
    elif inp_month == 11 :
        print("November" , inp_year , "has 30 days.")
    elif inp_month == 12 :
        print("December" , inp_year , "has 31 days.")  
        
main()        
