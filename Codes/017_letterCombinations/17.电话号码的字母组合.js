/*
 * @lc app=leetcode.cn id=17 lang=javascript
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var num2char={
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

    var rst=[]

    for(var i=0; i<digits.length; i++) {
        var num = digits[i];
        if(i==0){
            rst=num2char[num];
            continue
        }else{
            var copy=[]
            for(let j in rst) {
                for(let k in num2char[num]) {
                    copy.push(rst[j]+num2char[num][k])
                }
            }
            rst=copy
        }
    }

    return rst
};
// @lc code=end

