/*
 * @Author: Theo_hui
 * @Date: 2021-08-27 16:44:58
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=5 lang=javascript
 *
 * [5] 最长回文子串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {

    // 子函数
    var expend = function(s,left,right){
        while(left>=0 && right<s.length && s[left]==s[right]){
            left--
            right++
        }
        return [left+1,right-1]
    }

    //记录最佳
    best_l=best_r=0

    for(var i=0;i<s.length;i++){
        let [l1,r1] = expend(s,i,i)
        let [l2,r2] = expend(s,i,i+1)
        let [r,l] = (r1-l1)>(r2-l2)?[r1,l1]:[r2,l2]
        if((r-l)>(best_r-best_l)){
            best_l=l
            best_r=r
        }
    }

    return s.substring(best_l,best_r+1)
};
// @lc code=end

