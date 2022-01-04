#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        rst=[]
        for i,num in enumerate(digits):
            if i==0:
                rst=num_to_char[num]
                continue
            new=[]
            for char in num_to_char[num]:
                for old in rst:
                    new.append(old+char)
            rst=new
        
        return rst

# @lc code=end

