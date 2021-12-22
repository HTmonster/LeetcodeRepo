/*
 * @lc app=leetcode.cn id=16 lang=javascript
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    var almost=Infinity;

    nums.sort(function(a, b){return a - b}); 

    for (var i=0; i<nums.length-1; i++) {
        var left=i+1;
        var right=nums.length-1;
        while(left<right) {
            sum=nums[i]+nums[left]+nums[right];

            if(sum>target){
                right--;
            }else if(sum==target) {
                return target;
            }else{
                left++;
            }
            if(Math.abs(sum-target)<Math.abs(almost-target)){
                almost=sum;
            }
        }
    }

    return almost;

};
// @lc code=end

