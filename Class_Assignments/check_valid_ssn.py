"""
Input      : Prompt user to enter an SSN (ddd-dd-dddd)
Conditions : 
    a. Length should be 11 and delimeter "-" at 3rd and 6th position
    b. Should be numeric
    c. Area code (first 3) not equal to 000,666 and not between 900-999
    d. Group code should not be 00
    e. Serial nbr should not be 0000

"""

ssn = input("Enter an ssn in format ddd-dd-dddd :")
    
ssn_replace = ssn.replace('-','')

# Function to check for 3 group conditions !!!
def ssn_groups(ssn) :     
    ssn_chunks = ssn.split('-')
    area       = ssn_chunks[0]
    group      = ssn_chunks[1]
    serial_nbr = ssn_chunks[2]
    
    if area not in ('000','666') and area[0] != '9' \
    and group !=  '00' \
    and serial_nbr !=  '0000':
        return (True)
    else :
        return (False)

# Length & format check + numeric check + group conditions check
if (len(ssn) == 11 and ssn[3] == '-' and ssn[6] == '-' )\
    and ssn_replace.isnumeric() :
        if ssn_groups(ssn) is True :              # Calling function and checking for return value
           print ("Valid SSN")
        else:
           print ("Invalid SSN")
else :
    print ("Invalid SSN")