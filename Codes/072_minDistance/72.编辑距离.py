'''
Description: 
Autor: HTmonster
Date: 2022-03-04 16:11:53
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp(i,j)定义 word1[0,i]与word2[0,j]的最小编辑距离问题
        
        # 备忘录
        mem=dict()

        def dp(i,j):
            # 退出条件
            if i==-1: return j+1
            if j==-1: return i+1

            # 检查备忘录
            if (i,j) in mem.keys(): 
                return mem[(i,j)]
            if word1[i]==word2[j]:
                return dp(i-1,j-1)
            else:
                return min(
                    dp(i-1,j)+1,   # 删除
                    dp(i,j-1)+1,   # 增加
                    dp(i-1,j-1)+1) # 替换
        return dp(len(word1)-1,len(word2)-1)  
            

# @lc code=end

