/*
 * @lc app=leetcode.cn id=15 lang=javascript
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    var rst= new Array();
    var n=nums.length;
    if(n<3){return rst;}

    //排序
    nums.sort(function(a, b){return a - b})
    // console.log(nums)

    //单遍历
    for(var i=0;i<n;i++){
        if(i>0 && nums[i]==nums[i-1]){
            continue;
        }
        if(nums[i]>0){
            break;
        }
        //双指针
        var L=i+1;
        var R=n-1;
        while(L<R){
            var sum=nums[i]+nums[L]+nums[R];
            // console.log(i,L,R,sum)
            if(sum==0){
                rst.push([nums[i],nums[L],nums[R]])
                while(L<R && nums[L]==nums[L+1]){
                    L++
                }
                while(L<R &&nums[R]==nums[R-1]){
                    R--
                }
                // console.log(L,R)
                L++;
                R--;
            }else if(sum<0){
                L++
            }else{
                R--
            }
        }
    }

    return rst;

};
// @lc code=end

