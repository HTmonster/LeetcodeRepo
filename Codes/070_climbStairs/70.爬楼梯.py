'''
Description: 
Autor: HTmonster
Date: 2022-02-17 16:26:35
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0,1,2]
        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]
        
# @lc code=end

