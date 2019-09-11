# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 08:46:33 2019

@author: wangpeng884112
"""

'''
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
solution_!: Divide the array into two part, larger than zero or smaller than zero, and select number from two parts
results:
    Time Limit Exceeded
311/313 cases pass
'''
class Solution1:
    def threeSum(self, nums):
        record = []
        if nums == [] or len(nums) < 3:
            return record
        self.quicksort(nums,0,len(nums)-1)
        flag = -1
        for i in range(0,len(nums)):
            if nums[i] > 0:
                flag = i
                break
        if flag == -1:
            flag = len(nums)
            
        # consider a extreme situation, all the selected nums are 0
        if nums[flag-1] == nums[flag-2] == nums[flag-3] == 0:
            record.append([0,0,0])
        
        # split the list into two part: <=0 or >0
        less = nums[0:flag][::-1]
        large = nums[flag::]
        
        # select two number from "less" and one number from "large"
        i = 0
        flag = 0
        while i < len(less):
            j = i + 1
            k = 0
            while j < len(less):
                if k == len(large):
                    break
                if less[i] + less[j] + large[k] == 0:
                    record.append([less[i],less[j],large[k]])
                    flag = flag + 1
                    j = j + 1
                    k = k + 1
                elif less[i] + less[j] + large[k] > 0:
                    j = j + 1
                elif less[i] + less[j] + large[k] < 0:
                    k = k + 1          
            i = i + 1

        # select two number from "large" and one number from "less"
        i = 0
        k = 0
        flag = 0
        while i < len(large):
            j = i + 1
            k = 0
            while j < len(large):
                if k == len(less):
                    break
                if large[i] + large[j] + less[k] == 0:
                    record.append([less[k],large[i],large[j]])
                    flag = flag + 1
                    j = j + 1
                    k = k + 1
                elif large[i] + large[j] + less[k] < 0:
                    j = j + 1
                elif large[i] + large[j] + less[k] > 0:
                    k = k + 1
            
            i = i + 1
        
        record = self.remove_repeat(record)  # remove the repeat item
        
        
        return record
    
    def remove_repeat(self, record):
        list_record = []
        for i in record:
            if i not in list_record:
                list_record.append(i)    
        return list_record
        
        
    def quicksort(self, nums,low,high):
        if low < high:
            flag = self.partitial(nums,low,high)
            self.quicksort(nums, low, flag - 1)
            self.quicksort(nums, flag + 1, high)
            
        
        
    def partitial(self, nums,low,high):
        flag = low
        big_num = nums[high]   # set the last number as the partitial number
        for i in range(low,high):
            if nums[i] < big_num:   # if the number should be set on the right set of the partitial number
                nums[i], nums[flag] = nums[flag], nums[i] #iteratively change the site
                flag = flag + 1
        nums[high],nums[flag] = nums[flag],nums[high]   #set he partitial number on the right position
        return flag
        
class Solution:
    def threeSum(self, nums):
        record = []
        
    
    def remove_repeat(self, record):
        list_record = []
        for i in record:
            if i not in list_record:
                list_record.append(i)    
        return list_record
        
        
    def quicksort(self, nums,low,high):
        if low < high:
            flag = self.partitial(nums,low,high)
            self.quicksort(nums, low, flag - 1)
            self.quicksort(nums, flag + 1, high)
            
        
        
    def partitial(self, nums,low,high):
        flag = low
        big_num = nums[high]   # set the last number as the partitial number
        for i in range(low,high):
            if nums[i] < big_num:   # if the number should be set on the right set of the partitial number
                nums[i], nums[flag] = nums[flag], nums[i] #iteratively change the site
                flag = flag + 1
        nums[high],nums[flag] = nums[flag],nums[high]   #set he partitial number on the right position
        return flag        

test = Solution()
arr = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
record = test.threeSum(arr)
        
