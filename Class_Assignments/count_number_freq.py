"""
Neha Bais

Write a program that generates 1,000 random integers
between 0 and 9 and displays the count for each number.

"""

import random

N = 1000

# Empty list to store random integers
rand_int = []

# count list ranging from 0 to 9
count_int = [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

# Get random integers
for i in range(N) :
    x = random.randint(0,9)
    rand_int.append(x)

# Check for occurence of a number
for  e in count_int:
    count = 0
    for i in rand_int :
        if i == e :
            count = count + 1
    print(e , 'occurs' , count , 'times.')        