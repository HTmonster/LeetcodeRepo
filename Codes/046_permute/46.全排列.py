'''
Description: 
Autor: HTmonster
Date: 2022-03-22 11:04:06
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    # API 法
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     import itertools

    #     return list(itertools.permutations(nums,len(nums)))
    
    # 回溯法
    def permute(self, nums: List[int]) -> List[List[int]]:
        rst=[] # 结果数组

        def backtrack(l,choices):
            # 退出条件+结果存储
            if len(choices)==0:
                rst.append(l[:])
            # 遍历 做选择
            for i,num in enumerate(choices):
                l.append(num)
                backtrack(l,choices[:i]+choices[i+1:])
                l.pop()
        backtrack([],nums)
        return rst


# @lc code=end

