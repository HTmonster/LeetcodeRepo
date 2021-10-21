#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
from typing import Any


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #1. 作弊方法
        # return re.match(r'^{}$'.format(p),s)!=None
        #2. 递归法  没有剪枝 时间消耗比较大
        # 递归 匹配子处理函数
        # def sub_ismatch(s,p):
        #     len_s,len_p=len(s),len(p)
            
        #     if len_p==0:return len_s==0 # 匹配式以及完了
        #     # 字符串已经匹配完
        #     if len_s==0:return sub_ismatch(s,p[2:]) if (len_p>=2 and p[1]=="*") else False

        #     # 当前的字符
        #     char_s,char_p=s[0],p[0]
        #     #分情况 包含任意匹配字符
        #     if len_p>=2 and p[1]=='*':
        #         # 匹配了
        #         if char_s==char_p or char_p=='.':
        #             # 两种情况分别测试
        #             match_list=[]
        #             match_list.append(sub_ismatch(s,p[2:])) #此次不匹配
        #             match_list.append(sub_ismatch(s[1:],p)) #此次匹配
        #             # 判断
        #             return any(match_list)
        #         else:
        #             # 只能试一试跳过此次匹配
        #             return sub_ismatch(s,p[2:])
        #     else:
        #         # 单个字符匹配 推进
        #         if char_s==char_p or char_p=='.':
        #             return sub_ismatch(s[1:],p[1:])
        #         # 不匹配 匹配终止
        #         else:
        #             return False
        # return sub_ismatch(s,p)
        # 3. 动态规划法 使用空间换时间

        len_s,len_p = len(s),len(p)

        #创建存储数组
        ds=[[False,]*(len_p+1) for _ in range(len_s+1)]
        ds[0][0]=True
        
        def match(i,j):
            if i==0 or j==0:
                return False
            if p[j-1]=="." or s[i-1]==p[j-1]:
                return True
            return False

        for i in range(len_s+1):
            for j in range(1,len_p+1):
                # 特殊情况 "*"
                if p[j-1]=="*":
                    ds[i][j]=any(
                        [
                            ds[i][j-2],                         #不匹配，排除这两个字符
                            match(i,j-1) and ds[i-1][j]         #匹配，必须匹配，状态同上一个字符
                        ])
                else:
                    ds[i][j]=all([match(i,j),ds[i-1][j-1]])     #必须此次匹配 且前面的都匹配了

        print(ds)
        return ds[len_s][len_p]
# @lc code=end

