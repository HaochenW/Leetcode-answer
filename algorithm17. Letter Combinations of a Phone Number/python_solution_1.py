# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:32:34 2019

@author: wangpeng884112
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        module = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        i = 0
        now_str = []
        while i < len(digits):
            next_str = module[int(digits[i])-2]
            if now_str = []:
                for i in range(1,len(next_str)):
                    now_str.append(next_str[i])
            
            
            i = i + 1