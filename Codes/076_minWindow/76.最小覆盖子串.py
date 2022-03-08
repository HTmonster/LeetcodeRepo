'''
Description: 
Autor: HTmonster
Date: 2022-02-18 11:21:39
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        charIndex={}   # 字符索引
        need=[]
        i=0
        for c in t:
            if c not in charIndex.keys():
                charIndex[c]=i
                i+=1
                need.append(1)
            else:
                need[charIndex[c]]+=1

        # 结果开始点 和结尾
        res_left,res_right=0,float("inf")

        left,right=0,0 # 左右指针  window=[left,right]
        containCnt=[0 for _ in range(len(charIndex.keys()))]  # 包含的字符计数

        def check():
            nonlocal need,check
            for i in range(len(need)):
                if need[i] > containCnt[i]:
                    return False
            return True

        while right <len(s):
            #1. 右边先行 直到包含所有字符串后停止
            while not check() and right < len(s):
                if s[right] in t: containCnt[charIndex[s[right]]]+=1
                right+=1
            
            # print([left, right,s[left:right]],containCnt)

            #2. 左边收缩 尝试最小的范围
            while check() and left< len(s):
                if s[left] in t: containCnt[charIndex[s[left]]]-=1
                #更新值
                if right-left<res_right-res_left:
                    res_left,res_right =left,right

                left +=1
                # print("*", [left, right,s[left:right]],containCnt)
        
        if res_right==float("inf"):
            return ""
        else:
            return s[res_left:res_right]
# @lc code=end

