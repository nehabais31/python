"""
Neha Bais

Calculates gratuity nd total from gratuity rate and subtotal entered by User !!!

"""

gratuity_rate = eval(input("Enter a gratuity rate in % : "))
subtotal      = eval(input("Enter the subtotal : "))

gratuity = (gratuity_rate * subtotal) / 100
total    = subtotal + gratuity

print ("The gratuity is", gratuity, "and total is", total)