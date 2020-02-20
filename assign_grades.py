"""
Neha Bais
MET CS-521 Spring'20

Assignment 10.1 

reads a list of scores and then assigns grades
based on the following scheme:
The grade is A if score is best – 10.
The grade is B if score is best – 20.
The grade is C if score is best – 30.
The grade is D if score is best – 40.
The grade is F otherwise.

"""

def get_grade(lst_scores,best) :
    for i in range(0 , len(lst_scores)) :
        if lst_scores[i] >= best - 10 :
            grade = "A"        
        elif lst_scores[i] >= best - 20 :
            grade = "B"
        elif lst_scores[i] >= best - 30 :
            grade = "C"
        elif lst_scores[i] >= best - 40 : 
            grade = "D"
        else :
            grade = "F"
            
        print ("Student " , i , "score is " , lst_scores[i] ,
            "and grade is " , grade)
            
            
def main() :
    
    x =  input("Enter scores separated by spaces : ")
    scores = x.split()                              # converting entered string into list
    lst_scores = [eval(e) for e in scores]          # Converting the scores in integers
    best = max(lst_scores)
    get_grade(lst_scores,best)
    
main()    
