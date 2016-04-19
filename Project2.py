'''
Created on Apr 16, 2016

@author: Brianna
'''
import sys
sys.argv
# with open('cost_matrix_proj2.txt') as f:
#     for line in f:
#         a, b ,c, d = [int(i) for i in line.split()]
#         print (a,b,c,d)
# file = open('cost_matrix_proj2.txt','r') ##open the cost marix file as read only
# 
# f= print (file.readlines()) ##print each line read
# 
# def permute(a, results):
#     if len(a) == 1:
#         results.insert(len(results), a)
# 
#     else:
#         for i in range(0, len(a)):
#             element = a[i]
#             a_copy = [a[j] for j in range(0, len(a)) if j != i]
#             subresults = []
#             permute(a_copy, subresults)
#             for subresult in subresults:
#                 result = [element] + subresult
#                 results.insert(len(results), result)
# 
# results = []
# permute(range(len(f)), results) # [0, 1, 2] for a 3x3 matrix
# file.close() ##close the file