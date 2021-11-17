/*
 * @lc app=leetcode.cn id=11 lang=javascript
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {

    var left=0,right=height.length-1;
    var max_value=-1;

    while(left<right){
        var left_value=height[left];
        var right_value=height[right];

        var value
        if(left_value>right_value){
            value=(right-left)*right_value
            right--;
        }else{
            value=(right-left)*left_value
            left++;
        }

        if(value>max_value){
            max_value=value
        }
    }

    return max_value;

};
// @lc code=end

