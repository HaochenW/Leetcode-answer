# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:03:56 2019

@author: haochen01.wang
"""

'''
Edition I
Idea: search all the position, checking the longest palindrome substring on that position;
results: Time Limit Exceeded
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return s
        string = s[0]
        len_str = 1
        i = 0
        while i < len(s):
            start,end = self.isPalindromic(s,i,i)  # Start from the current character, search for the Palindromic substring
            if end - start + 1 > len_str:
                string = s[start:end+1]
                len_str = end - start + 1
            i = i + 1
        return string
    
    
    def isPalindromic(self, s,start,end):
#        if start != 0:
#            if s[start-1] == s[end+1]:
#                length = length + 2
#                start = start - 1
#                end = end - 1
#                now_length = isPalindromic(s,start,end,length)
#            else:
#                return max(length,now_length)
        while 1:
            if end == len(s) - 1:
                break
            if self.isequal(s[start:end+1]) and s[end+1] == s[end]:
                end = end + 1
            elif start != 0 and s[start-1] == s[end+1]:
                start = start - 1
                end = end + 1
            else:
                break      
        return start,end
        

        
    def isequal(self,string):
         l = len(string)
         i = 0
         flag = True
         while i < l - 1:
             if string[i] != string[i+1]:
                 flag = False
             i = i + 1
         return flag
        
        
        
        
        
        
        
        
        
        
        
s = "abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa"
test = Solution()
string = test.longestPalindrome(s)