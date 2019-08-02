# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:34:52 2019

@author: haochen01.wang
"""


'''
edition I: 
Idea: If the next character not appear in the record string, then we will add the character into record string;
      If the next character appear in the record string, then we will discard the first character in the record string, then add the next character;
results: wrong;
situation: "pwwkew"
why？： The sequence must be started from the repeated position, not the start position;
        Besides, we must record the longest string before the next character
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_str = ''
        i = 0
        while i < len(s):
            if s[i] in tmp_str:
                tmp_str = tmp_str[1::] + s[i]
            else:
                tmp_str = tmp_str + s[i]
            i = i + 1
        return len(tmp_str)
'''

'''
edition II: changed from edition I
result:  faster than 74.06% of Python3 online submissions for Longest Substring Without Repeating Characters.
         less than 5.09% of Python3 online submissions for Longest Substring Without Repeating Characters.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_str = ''
        i = 0
        max_len = 0
        while i < len(s):
            if s[i] in tmp_str:
                pos = tmp_str.index(s[i])
                if len(tmp_str) > max_len:    # record the maximum length
                    max_len = len(tmp_str)
                tmp_str = tmp_str[pos+1::] + s[i]  # make the new string from the next character of the repeated character
            else:
                tmp_str = tmp_str + s[i] 
            i = i + 1
            
        if len(tmp_str) > max_len:
            max_len = len(tmp_str)
            
        return max_len
    

s = "pwwkew"
test = Solution()
length = test.lengthOfLongestSubstring(s)


'''
思路说明：其实核心的想法就是，当扫描过后这个位置的子串后，后面的子串可以用前面的最长子串迭代得到；只需要记录下来长度最长的子串即可；有点类似于动态规划的想法，把问题拆解；
'''