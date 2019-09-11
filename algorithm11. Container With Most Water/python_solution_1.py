# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:07:47 2019

@author: wangpeng884112
"""

'''
edition1 
Method: Just brute forcely search all the results
'''

class Solution1:
    def maxArea(self, height) -> int:
        i = 0 
        max_area = 0
        while i < len(height) - 1:
            j = i + 1
            while j < len(height):
                start = height[i]
                end = height[j]
                area = min(start,end) * (j - i)
                if area > max_area:
                    max_area = area
                j = j + 1
            i = i + 1        
        return max_area
    
    

class Solution2:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while 1:
            if left != right:
                area = (right - left) * min(height[left],height[right])
                if area > max_area:
                    max_area = area
            else:
                break
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        
        return max_area

        
        
        
input_list = [1,8,6,2,5,4,8,3,7]
test = Solution2()
answer = test.maxArea(height = input_list)