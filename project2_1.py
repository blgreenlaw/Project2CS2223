'''
Created on Apr 16, 2016

@author: Brianna Greenlaw
Project 2 for CS2223
Program both a greedy algorithm and exhaustive search
for the Assignment Program, which finds the optimal 
value for a cost matrix
'''
##This part is reading in the file with the cost matrix
##and splitting the data into the distinct lines.
with open('input.txt') as f:
    cminput = [[int(x) for x in ln.split(',')] for ln in f]
    print ("Matrix input: \n", cminput)
     
import sys
import time

##setting the matrix equal to the given, properly read matrix data
matrix = cminput
      
def cost_matrix_es(a, results):
    if len(a) == 1: ##If the matrix is one element return that element
        results.insert(len(results), a)

    else: ##Exhaustive Search for cost matrix
        for i in range(0, len(a)):
            element = a[i]
            a_copy = [a[j] for j in range(0, len(a)) if j != i]
            subresults = []
            cost_matrix_es(a_copy, subresults)
            for subresult in subresults:
                result = [element] + subresult
                results.insert(len(results), result)

results = []
cost_matrix_es(range(len(matrix)), results) # [0, 1, 2, 3] for a 4x4 matrix

##Finding the minimum cost of the matrix
n = len(matrix)
minval = sys.maxsize
for row in range(n):
    cost = 0
    for col in range(n):
        cost += matrix[row][col]
    minval = min(cost, minval)

print ("The minimum cost of the matix is: \n", minval)

##Calculating the time taken to run the exhaustive search program
start_time = time.clock()
cost_matrix_es(matrix,results)  ##Runs the recusive program while timing
print("The time taken to run the exhaustive search: \n---%s seconds ---" % (time.clock() - start_time))