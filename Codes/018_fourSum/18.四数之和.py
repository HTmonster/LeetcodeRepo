'''
Description: 
Autor: HTmonster
Date: 2022-01-25 09:52:10
'''
#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序 O(nlogn)
        nums=sorted(nums)

        # 结果数组
        result=[]
                    
        #遍历 O(n^3)
        for left in range(len(nums)-3):
            # 去重
            if left>0 and nums[left]==nums[left-1]:
                continue
            for mid_left in range(left+1,len(nums)-2):
                # 去重
                if mid_left>left+1 and nums[mid_left]==nums[mid_left-1]:
                    continue
                # 双指针之和
                sum2=nums[left]+nums[mid_left]

                # 内双指针
                mid_right,right=mid_left+1,len(nums)-1
                while mid_right<right:
                    
                    # 内循环总和
                    inner_sum2=nums[mid_right]+nums[right]
                    if inner_sum2+sum2>target:
                        right-=1
                    elif inner_sum2+sum2<target:
                        mid_right+=1
                    else:
                        result.append([
                            nums[left],
                            nums[mid_left],
                            nums[mid_right],
                            nums[right]
                            ])

                        right-=1
                        mid_right+=1
                        while right>mid_right and nums[right]==nums[right+1]:
                            right-=1
                        while right>mid_right and nums[mid_right]==nums[mid_right-1]:
                            mid_right+=1
        return result
# @lc code=end

