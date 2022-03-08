'''
Description: 
Autor: HTmonster
Date: 2022-02-17 16:42:51
'''
#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlen=0

        for i in range(len(nums)-1):
            maxlen = max(maxlen, i+nums[i])
            if maxlen<=i:
                return False
        
        return maxlen>=len(nums)-1
            
# @lc code=end

