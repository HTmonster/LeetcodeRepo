'''
Description: 
Autor: HTmonster
Date: 2022-02-18 10:10:29
'''
#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0

        numSum=[0,]   # 存储前缀
        preSum={0:1}  # 存储前缀的个数
        for i,num in enumerate(nums):
            sum = numSum[i]+num  # 自己的前缀和
            numSum.append(sum)

            need = sum-k         # 需要的值 即为k

            # 计算个数
            if need in preSum.keys():
                res+=preSum[need]
            
            # 更新自己
            if sum in preSum.keys():
                preSum[sum]+=1
            else:
                preSum[sum]=1

        # print(numSum,preSum)
            
        return res


# @lc code=end

