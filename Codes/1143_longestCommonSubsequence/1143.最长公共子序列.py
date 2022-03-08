'''
Description: 
Autor: HTmonster
Date: 2022-02-17 15:41:39
'''
#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 数组
        dp=[[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        ans=0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

                ans=max(dp[i+1][j+1],ans)
        return ans
        
# @lc code=end

