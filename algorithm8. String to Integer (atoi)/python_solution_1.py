# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:26:52 2019

@author: haochen01.wang
"""

'''
Edition I
It is a bad example of accepted answer, only forcely pass all the cases.
'''
class Solution:
    def myAtoi(self, str: str) -> int:
        i = 0
        record_str = ''
        while i < len(str):
            if str[i] == ' ':
                i = i + 1
                continue
            else:
                break
        
        str = str[i::]
        i = 0
        while i < len(str):
            if self.isNum(str[i]) == -1:
                break
            else:
                record_str = record_str + str[i]            
            i = i + 1
        
                
        if record_str == '':
            return 0
        elif record_str[0] == '+':
            record_str = '+' + self.cut_string(record_str[1::])
            if len(record_str) == 1:
                return 0
            if int(record_str[1::]) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(record_str[1::])
        elif record_str[0] == '-':
            record_str = '-' + self.cut_string(record_str[1::])
            if len(record_str) == 1:
                return 0
            if -int(record_str[1::]) < -2**31:
                return -2**31
            else:
                return -int(record_str[1::])
        else:
            record_str = self.cut_string(record_str)
            if int(record_str) > 2**31 - 1:
                return 2**31 - 1
            elif int(record_str) < -2**31:
                return -2**31
            else:
                return int(record_str)
        
            
    
    def isNum(self, char):
        try:
            if char != '+' and char != '-' and char != ' ':
                _ = int(char)
                return char
            else:
                return char
        except:
            return -1
    
    def cut_string(self, record_str):
        try:
            i = 0
            while i < len(record_str):   
                _ = int(record_str[i])
                i = i + 1
            return record_str
        except:
            return record_str[0:i]
            
        
test = Solution()
string = test.myAtoi("   +0 123")