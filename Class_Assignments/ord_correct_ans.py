# -*- coding: utf-8 -*-
"""
Neha Bais

(Sort students by grades) Rewrite Listing 11.2, GradeExam.py, to display the students
in increasing order of the number of correct answers.

"""

def sort_result(result) :
    # Sorting on correct count
    for i in range (0,len(result)) :
        for j in range (0,len(result)-1) :
            if (result[j][1] > result[j+1][1]) :
                temp = result[j]
                result[j] = result[j+1]
                result[j+1] = temp
                
    return (result)            

def main() :
    # Students' answers
    answers = [
       ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
       ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
       ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
       ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
       ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
       ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
       ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
       ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
       
    # keys to questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    
    #Empty list to capture students and their correct ans
    result = []    
    
    # Check for correct ans
    for i in range(len(answers)) :
        correct_count = 0
        for j in range (len(answers[i])) :
            if answers[i][j] == keys[j] :
                correct_count += 1
        res_sublist = [i,correct_count]
        result.append(res_sublist)
    
    #sorting the output on the basis of correct count    
    sort_result(result)
    
    #print output
    for i in range (len(result)) :
        print("Student", result[i][0] , "'s correct count is ", result[i][1])

main()        