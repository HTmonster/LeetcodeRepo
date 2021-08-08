/*
 * @lc app=leetcode.cn id=1 lang=javascript
 *
 * [1] 两数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
//1. 暴力遍历法
// var twoSum = function(nums, target) {
//     for(var i=0;i<nums.length-1;i++){
//         for(var j=i+1;j<nums.length;j++){
//             if(nums[i]+nums[j]==target){
//                 return [i,j]
//             }
//         }
//     }
// };

//2. hash表法
var twoSum = function(nums, target){
    hashT = new Map();
    for(var i=0;i<nums.length;i++){
        v=hashT.get(target-nums[i])
        if(typeof v == 'number'){
            return [i,v]
        }
        else{
            hashT.set(nums[i],i)
        }
    }
};
// @lc code=end

