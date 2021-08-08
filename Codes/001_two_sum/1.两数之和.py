'''
Author: Theo_hui
Date: 2021-08-08 20:06:43
Descripttion: 
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    # 1. 暴力遍历法
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j]==target:
    #                 return [i,j]

    # 2. 哈希表法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashT = {}

        for i,v in enumerate(nums):
            if target-v in hashT.keys():
                return [i,hashT[target-v]]
            else:
                hashT[v]=i
# @lc code=end

