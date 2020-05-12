"""
Calculate sales amount based on below scheme 
    Sales Amount          Commission Rate
    $0.01–$5,000           8 percent
    $5,000.01–$10,000      10 percent
    $10,000.01 and above   12 percent

and sisplay the table for sales starting from
10000 to 100000    
    
@author: Neha Bais
MET CS-521 A3

"""


def compute_commission(sales_amnt):
    '''
    Calculate sales amount based on below scheme 
    Sales Amount          Commission Rate
    $0.01–$5,000           8 percent
    $5,000.01–$10,000      10 percent
    $10,000.01 and above   12 percent
    
    '''
    amount = 0
    commission = 0
    
    if sales_amnt > 0.01 :
        if sales_amnt < 5000:
            amount = sales_amnt
        else :
            amount = 5000
        commission = commission + (amount * 0.08 )
            
    if sales_amnt >=  5000.01:
        if sales_amnt < 10000:
            amount = sales_amnt - amount
        else:
            amount = 5000
        commission = commission + (amount * 0.1 )    
            
    if sales_amnt >= 10000.01:
        amount = sales_amnt - 10000
        commission = commission + (amount * 0.12 )
    
    return commission
    
def main():
    sales_amnt = 10000
    print('Sales Amount' , '\t', 'Commission')
    while (sales_amnt <= 100000):
        commission = compute_commission(sales_amnt)
        print(sales_amnt , '\t\t' , commission)
        sales_amnt = sales_amnt + 5000
        
main() 