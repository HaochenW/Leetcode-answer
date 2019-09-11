# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 08:42:43 2019

@author: wangpeng884112
"""


'''
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
'''
'''
python_solution_1
just directly judge the condition

Results: Not good
Runtime: 72 ms, faster than 8.88% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.1 MB, less than 5.38% of Python3 online submissions for Roman to Integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        flag = 0
        while 1:
            if s[flag:flag+2] == 'CM':
                num = num + 900
                flag = flag + 2
            elif s[flag:flag + 2] == 'CD':
                num = num + 400
                flag = flag + 2
            elif s[flag:flag+2] == 'XC':
                num = num + 90
                flag = flag + 2
            elif s[flag:flag+2] == 'XL':
                num = num + 40
                flag = flag + 2
            elif s[flag:flag+2] == 'IX':
                num = num + 9
                flag = flag + 2
            elif s[flag:flag+2] == 'IV':
                num = num + 4
                flag = flag + 2
            elif s[flag] == 'M':
                num = num + 1000
                flag = flag + 1
            elif s[flag] == 'D':
                num = num + 500
                flag = flag + 1
            elif s[flag] == 'C':
                num = num + 100
                flag = flag + 1
            elif s[flag] == 'L':
                num = num + 50
                flag = flag + 1
            elif s[flag] == 'X':
                num = num + 10
                flag = flag +1
            elif s[flag] == 'V':
                num = num + 5
                flag = flag + 1
            else:
                num = num + 1
                flag = flag + 1
            
            if flag >= len(s):
                return num

test = Solution()
num = test.romanToInt('MCMXCIV')
            
            

