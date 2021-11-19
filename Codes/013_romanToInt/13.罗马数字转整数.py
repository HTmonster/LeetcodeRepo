#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMANS={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        last=num=ROMANS[s[0]]
        for i in range(1,len(s)):
            now=ROMANS[s[i]]
            if now >last:
                now=now-2*last
            num+=now
            last=now
        return num
# @lc code=end

