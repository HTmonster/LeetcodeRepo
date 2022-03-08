'''
Description: 
Autor: HTmonster
Date: 2022-02-17 14:36:53
'''
#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
import re


class Solution:
    # 动态规划法
    # def findLength(self, nums1: List[int], nums2: List[int]) -> int:
    #     # 根据长度申请一个二维数组
    #     dp=[[0 for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]

    #     # 二重循环
    #     ans=0
    #     for i in range(len(nums1)):
    #         for j in range(len(nums2)):
    #             # 相等则加1
    #             if nums1[i] == nums2[j]:
    #                 dp[i+1][j+1]=dp[i][j]+1
    #             else:
    #                 dp[i+1][j+1]=0
    #             ans=max(ans,dp[i+1][j+1])
    #     return ans

    # 滑动窗口法
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        ans=0
        cursor1,cursor2=0,len(nums2)-1

        while cursor2>0:
            # 统计 窗口大小
            window=0
            i,j=cursor1,cursor2
            while i<len(nums1) and j<len(nums2):
                window=window+1 if nums1[i]==nums2[j] else 0
                i+=1
                j+=1
                ans=max(ans,window)
            #游标移动
            cursor2-=1
            
        
        while cursor1<len(nums1):
            # 统计 窗口大小
            window=0
            i,j=cursor1,cursor2
            while i<len(nums1) and j<len(nums2):
                window=window+1 if nums1[i]==nums2[j] else 0
                i+=1
                j+=1
                ans=max(ans,window)
            #游标移动
            cursor1+=1
            
        
        return ans



# @lc code=end

