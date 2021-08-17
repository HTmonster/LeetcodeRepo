/*
 * @Author: Theo_hui
 * @Date: 2021-08-17 10:59:52
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=3 lang=javascript
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let res=0, left=-1
    let c_maps = new Array()

    for(var right=0;right<s.length;right++){
        c_i=c_maps[s[right]]

        if(typeof(c_i) != "undefined" && c_i>left){
            left = c_i
        }else{
            let new_res = right-left
            if(new_res>res){
                res=new_res
            }
        }
        c_maps[s[right]]=right
    }

    return res
};
// @lc code=end

