'''
Author: Theo_hui
Date: 2021-09-08 19:11:15
Descripttion: 
'''
#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    # 1. 状态扫描法
    # def myAtoi(self, s: str) -> int:    
    #     #记录的结果与符号
    #     rst,symbol=0,1
    #     status=0 #0,1,2
    #     i=0
    #     while i<len(s):
    #         #取字符           
    #         c=s[i]
    #         # print(i,c)
    #         #状态0：去除空格
    #         if status==0:
    #             if c==' ':
    #                 i+=1
    #             else:
    #                 # 状态转换
    #                 status=1
    #         #状态1：符号判断
    #         elif status==1:
    #             if c=="+":
    #                 i+=1
    #             elif c=="-":
    #                 i+=1
    #                 symbol=-1
    #             status=2
    #         #状态2：数字解析
    #         elif status==2:
    #             if '0'<=c<='9':
    #                 rst=rst*10+int(c)
    #                 # print(rst)
    #                 i+=1
    #             else:
    #                 break
    #             if symbol==1 and rst>(2**31-1):
    #                 rst=2**31-1
    #                 break
    #             if symbol==-1 and rst>2**31:
    #                 rst=2**31
    #                 break
    #     # print(rst)
    #     return rst*symbol
    # 2. 正则表达式法
    def myAtoi(self, s: str) -> int:
        return min(max(int(*re.findall("^\s*[\+\-]?\d+",s)),-(2**31)),2**31-1)

# @lc code=end

