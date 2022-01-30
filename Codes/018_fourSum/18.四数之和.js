/*
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-01-25 12:17:54
 */
/*
 * @lc app=leetcode.cn id=18 lang=javascript
 *
 * [18] 四数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    // 排序
    nums=nums.sort(function(a, b){return a - b})
    // 结果
    var result = new Array();

    for (var i = 0; i <nums.length-3; i++) {
        if(i>0 && nums[i]==nums[i-1]){ continue; }

        for (var j = i+1; j <nums.length-2;j++){
            if( j>i+1 && nums[j]==nums[j-1]){ continue;}

            m=j+1
            n=nums.length-1
            while(m<n){
                sum=nums[i]+nums[j]+nums[m]+nums[n]
                if(sum<target){ m++}
                else if(sum>target){ n--}
                else{
                    result.push(new Array(nums[i],nums[j],nums[m],nums[n]))
                    m++
                    n--
                    while(m<n && nums[m]==nums[m-1]){m++;}
                    while(m<n && nums[n]==nums[n+1]){n--;}
                }
            }
        }
    }

    return result;

};
// @lc code=end

