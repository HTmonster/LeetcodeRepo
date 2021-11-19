#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ROMANS={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',5000:''}

        roman=""
        unit=1
        while num>0:
            a=num%10
            if a==4 or a== 9:
                roman=ROMANS[unit]+ROMANS[5*((a+1)//5)*unit]+roman
            else:
                roman=ROMANS[5*unit]*(a//5)+ROMANS[unit]*(a%5)+roman
            num=num//10
            unit=unit*10
        return roman
# @lc code=end

