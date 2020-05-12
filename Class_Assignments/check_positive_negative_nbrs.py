"""
Neha Bais

Input  : Unspecified number of integers
Output : Number of positives entered
         Number of negatives entered
         Total of all the numbers
         Average of the numbers

Condition : Terminate the pgm when user enters 0
         
"""

sum = count_positive = count_negative = 0

data = eval(input("Enter an integer (the input ends if it is 0) : "))

if data == 0 :
    print ("You didn't enter any number.")
else :
    while data != 0 :
        sum += data 
        if (data < 0) :
            count_negative += 1
        else :
            count_positive += 1
        data = eval(input("Enter an integer (the input ends if it is 0) :"))
 
    average = sum / (count_positive + count_negative)

    print ("\nThe number of positives is ", count_positive)
    print ("The number of negatives is ", count_negative)
    print ("The sum is ",sum) 
    print ("The average is ", round(average,3))