#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right=0,len(height)-1

        maxValue=-1

        while left<right:
            h_left,h_right=height[left],height[right]
            if h_left< h_right:
                value=(right-left)*h_left
                while h_left>=height[left] and left<len(height):
                    left+=1
            else:
                value=(right-left)*h_right
                while h_right>=height[right] and right>=0:
                    right-=1
            if value>maxValue: maxValue=value

        return maxValue
                
# @lc code=end

