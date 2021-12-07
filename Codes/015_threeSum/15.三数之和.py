#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    # version 1
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rst=[] #所有的结果数组
        n=len(nums)
        if n<3:return rst

        # 排序 O(nlogn)
        nums.sort()

        # 遍历 O(n) +双指针
        for i in range(n):
            # 重复元素跳过
            if i>0 and nums[i]==nums[i-1]:continue
            # 后续的数都是大于0的
            if nums[i] >0: return rst
            
            L,R= i+1,n-1
            # 找第三个
            while L<R:
                sum=nums[i]+nums[L]+nums[R]
                if sum==0:
                    rst.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L+=1
                    R-=1
                elif sum<0:
                    L+=1
                else: 
                    R-=1
        return rst

        
# @lc code=end

