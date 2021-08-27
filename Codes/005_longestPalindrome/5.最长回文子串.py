'''
Author: Theo_hui
Date: 2021-08-27 15:19:53
Descripttion: 
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    #1. 中心拓展法
    # def longestPalindrome(self, s: str) -> str:
    #     # 子函数，中心拓展函数
    #     def expend(left,right):
    #         while left>=0 and right<len(s) and s[left]==s[right]:
    #             left-=1
    #             right+=1
    #         return left+1,right-1
        
    #     #记录最大
    #     max_s,max_e = 0,0
    #     for i in range(len(s)):
    #         l1,r1 = expend(i,i)     #奇数拓展
    #         l2,r2 = expend(i,i+1)   #偶数拓展
    #         (li,ri) = (l1,r1) if (r1-l1)>(r2-l2) else (l2,r2)
    #         if (ri-li)>(max_e-max_s):
    #             max_e,max_s = ri,li
    #     return s[max_s:max_e+1]
    # 2. 动态规划法
    def longestPalindrome(self, s: str) -> str:
        s_len=len(s)
        if s_len<2:
            return s

        # 存储状态数组 status[i][j]=True表示 s[i:j+1]是回文字符串
        status =[[False]*s_len for _ in range(s_len)]
        for i in range(s_len):
            status[i][i]=True
        
        # 记录最佳值
        best_i,best_j=0,0

        # 遍历所有字符串长度
        for L in range(2,s_len+1):
            for i in range(s_len):
                j=i+L-1
                if j>=s_len:
                    break
                if s[i]!=s[j]:
                    status[i][j]=False
                else:
                    if j-i<3:
                        status[i][j]=True
                    else:
                        status[i][j]=status[i+1][j-1]
                if status[i][j] and (j-i)>(best_j-best_i):
                    best_j,best_i =j,i
        
        return s[best_i:best_j+1]
# @lc code=end

