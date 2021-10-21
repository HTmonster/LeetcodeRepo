/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x<0){
        return false
    }

    var str_x=x.toString();
    var i=str_x.length-1;
    var j=0;

    while(j<=i){
        if(str_x[i]!=str_x[j]){
            return false
        }
        j++;
        i--;
    }

    return true;
};
// @lc code=end

