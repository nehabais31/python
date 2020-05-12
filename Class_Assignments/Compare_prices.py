
"""
Neha Bais

Compare the price of 2 packages 

"""

weight_1 , price_1 = eval(input("Enter the weight and price of package 1 : " ))
weight_2 , price_2 = eval(input("Enter the weight and price of package 2 : " ))

price_per_pound_pkg1 = price_1 / weight_1

price_per_pound_pkg2 = price_2 / weight_2

if price_per_pound_pkg1 < price_per_pound_pkg2 :
    print("Package 1 has better price.")
elif price_per_pound_pkg1 > price_per_pound_pkg2 :
    print("Package 2 has better price.")
else :
    print("Both the packages have same price.")