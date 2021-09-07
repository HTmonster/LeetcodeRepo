'''
Author: Theo_hui
Date: 2021-09-07 09:20:53
Descripttion: 
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        #符号
        symbol=-1 if x<0 else 1
        x,rst=abs(x),0
        while x>0:
            rst=rst*10+(x%10)
            x=x//10
        rst=symbol*rst
        return rst if -1*2**31<=rst<=2**31-1 else 0
# @lc code=end

