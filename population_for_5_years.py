# -*- coding: utf-8 -*-
"""
Neha Bais

Write a program to display the population for each of the next five years. Assume the
current population is 312032486 and one year has 365 days.
"""

total_time = 3600 * 24 * 365           #calculate total seconds in a year

birth     = total_time // 7
death     = total_time // 13
immigrant = total_time // 45

current_population = 312032486
add_on_population  = birth + immigrant - death

for i in range (1 , 6) :
    current_population = current_population + add_on_population
    print ('Population for year' , i ,'is:' , current_population)