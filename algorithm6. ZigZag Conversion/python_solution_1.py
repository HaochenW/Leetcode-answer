# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:45:57 2019

@author: haochen01.wang
"""
'''
Edition I
Idea: give the matrix of zigzag, and read the new string from the zigzag matrix
results: Time Limit Exceeded
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        i = 0
        row = 0
        flag = 0 
        while 1:
            if i % 2 == 0:
                j = 0
                matrix.append([[] for _ in range(numRows)])
                while j < numRows:
                    if flag == len(s):
                        j = j + 1
                        continue
                    matrix[row][j] = s[flag]
                    j = j + 1
                    flag = flag + 1
                row = row + 1
            else:
                j = 0
                bias = numRows - 1
                while j < numRows - 2:
                    if flag == len(s):
                        matrix.append([[] for _ in range(numRows)])
                        j = j + 1
                        continue
                    matrix.append([[] for _ in range(numRows)])
                    matrix[row][bias-1] = s[flag]
                    flag = flag + 1    
                    row = row + 1
                    j = j + 1
                    bias = bias - 1
            i = i + 1
            if flag == len(s):
                break
        new_string = ''
        j = 0
        while j < len(matrix[0]):
            i = 0
            while i < len(matrix):
                if matrix[i][j] != []:
                    new_string = new_string + matrix[i][j]  
                i = i + 1
            j = j + 1
        return new_string
        



test = Solution()
string = test.convert(s = "PAYPALISHIRING", numRows = 4)