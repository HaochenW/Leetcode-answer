# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:12:07 2019

@author: wangpeng884112
"""


'''
Solution_1:
Direct way to implement the algorithm
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common_str = ''
        min_len = float('inf')
        for item in strs:
            if len(item) < min_len:
                min_len = len(item)
                
        if strs == [] or min_len == 0:
            return common_str
        locate = 0
        while 1:
            flag = 0
            for i in range(len(strs) - 1):
                if strs[i][locate] == strs[i+1][locate]:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0:
                common_str = common_str + strs[0][locate]
            else:
                break
            locate = locate + 1
            if locate == min_len:
                break
        return common_str

test = Solution()
strs = ["flower","flow","flight"]
common_str = test.longestCommonPrefix(strs)