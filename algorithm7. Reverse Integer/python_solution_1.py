# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 22:34:08 2019

@author: wangpeng884112
"""
'''
Edition I
Idea: Use the function in python
results: faster than 58.58% of Python3 online submissions for Reverse Integer.
** Not elegent
'''
class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        re_str = ''
        i = len(str_x)
        while i > 0:
            re_str = re_str + str_x[i-1]
            i = i - 1
        if re_str[-1] == '-':
            re_int = int(re_str[0:-1])
            re_int = -re_int
        else:
            re_int = int(re_str)
        MAX_NUM = 2**31 - 1
        MIN_NUM = -2**31
        if re_int < MIN_NUM or re_int > MAX_NUM:
            return 0
        return re_int
    
    