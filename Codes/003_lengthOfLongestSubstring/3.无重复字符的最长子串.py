'''
Author: Theo_hui
Date: 2021-08-17 10:18:10
Descripttion: 
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # 双指针 滑动窗口法
    def lengthOfLongestSubstring(self, s: str) -> int:
        res,left,c_dicts = 0,-1,{} #结果 左指针 字符最右下标

        for right,c in enumerate(s):
            # 如果该字符串出现在了记录中 且 其包含在窗口中
            if c in c_dicts.keys() and c_dicts[c] > left:
                # 更新左边
                left = c_dicts[c]
            else:
                # 更新结果
                res = max(res,right-left)
            # 记录字符最左位置
            c_dicts[c]=right
        return res

# @lc code=end

