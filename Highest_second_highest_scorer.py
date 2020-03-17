"""
Neha Bais

Write a program that prompts the user to enter the
number of students and each student’s score, and displays the highest and secondhighest
scores.

"""

num_of_students = int(input('Enter the number of students :'))

highest_score  = 0
second_highest = 0

for i in range(num_of_students) :
    name  = input('Enter name of student : ')
    score = input('Enter score of student : ')
    
    score = int(score)

    if score > highest_score :
        second_highest = highest_score
        highest_score  = score
        
        highest_scorer = [[name,highest_score]]
        
    elif score == highest_score :
         highest_scorer.append([name,score])
         
    elif score > second_highest :
         second_highest = score
         second_highest_scorer = [[name,score]]
         
    elif score == second_highest :
         second_highest_scorer.append([name,score])
         

#print loop
print('\nHighest Scorer : ')
for name,score in highest_scorer :
    print(name,score)

print('\nSecond Highest Scorer : ')
for name,score in second_highest_scorer :
    print(name,score)         