"""
Neha Bais

Create a table of kilograms to pound conversion

"""

print ("Kilograms \t Pound")

for i in range (1,200,2) :
    print (i,end = '')
    print("\t\t", format(i * 2.2, ".1f"), end = '')
    print()