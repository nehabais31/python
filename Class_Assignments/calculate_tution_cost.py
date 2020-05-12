"""
Neha Bais
MET CS-521 A3

Suppose that the tuition for a university
is $10,000 this year and increases 5% every year. 
Compute the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now.

"""


tution_current = 10000
total_tution = 0

for year in range(1,15) :
    tution_current = tution_current + (tution_current * 0.05)
    
    if year == 10 :
        # store tenth year tution cost
        tution_tenth_year = tution_current
    elif year > 10 :
        # compute 4 years tution starting from 10th year
        total_tution = total_tution + tution_current

print('Tution for 10 years is: $',round(tution_tenth_year,2) , \
'\nTution for 4 years starting from 10th year is: $',round(total_tution,2))