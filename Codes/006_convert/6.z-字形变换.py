'''
Author: Theo_hui
Date: 2021-09-06 09:43:41
Descripttion: 
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    #模拟填充法
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        # 创建存储数组
        storage = ["" for _ in range(numRows)]

        #开始模拟填充
        line,status=0,"down"
        for c in s:
            # 填充
            storage[line]+=c         
            # 状态转换
            if status == "down":
                if line==numRows-1:
                    status="slant" #斜向上
                    line-=1
                else:
                    line+=1
            elif status == "slant":
                if line==0:
                    status="down"
                    line+=1
                else:
                    line-=1
        # print(storage)

        # 读取
        rst = "".join(storage)
        return rst
                


# @lc code=end

