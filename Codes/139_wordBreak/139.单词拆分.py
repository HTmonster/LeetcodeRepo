'''
Description: 
Autor: HTmonster
Date: 2022-03-22 10:20:35
'''
#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # 使用备忘录
        mem={} #idx:bool 位置及s[idx:]的匹配情况

        # 子问题
        def __word_break(idx):
            # 退出条件
            if idx>len(s)-1: return True

            # 直接结果返回
            if idx in mem.keys():
                return mem[idx]
            # 遍历每个词
            rst=False
            for w in wordDict:
                # 问题在于 拆不拆
                if s[idx:].startswith(w):
                    rst= rst or __word_break(idx+len(w))
                    if rst: break
            mem[idx]=rst
            return rst

        return __word_break(0)
# @lc code=end

