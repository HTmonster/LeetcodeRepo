#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        almost=float("inf") #最接近的值 初始为无穷

        #0.先排序 时间复杂度O(n^2)
        nums.sort()
        
        #1. 单层遍历+双指针逼近 时间负载度O(n*n)
        for i in range(len(nums)-1):
            left,right=i+1,len(nums)-1
            
            while left<right:

                Sum=nums[i]+nums[left]+nums[right] #本轮的和

                # 更新全局值
                if abs(Sum-target)<abs(almost-target):almost=Sum
                
                # 判断与目标的大小关系
                if Sum<target: 
                    left+=1
                elif Sum==target:
                    return target
                else:
                    right-=1
                # print(i,left,right,Sum,almost)
        return almost
# @lc code=end

