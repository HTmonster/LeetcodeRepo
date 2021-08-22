/*
 * @Author: Theo_hui
 * @Date: 2021-08-22 17:20:16
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=4 lang=javascript
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {

    //递归函数
    var getKth = function(nums1,nums2,s1,s2,k){
        var len1 = nums1.length-1-s1
        var len2 = nums2.length-1-s2
        //递归出口
        if(len1==0){
            return nums2[s2+k]
        }
        if(len2==0){
            return nums1[s1+k]
        }
        if(k==1){
            return Math.min(nums1[s1+1],nums2[s2+1])
        }else{
            var midk = Math.floor(k/2)
            var c1 = Math.min(midk,len1)
            var c2 = Math.min(midk,len2)
            if(nums1[s1+c1]<nums2[s2+c2]){
                k-=c1
                s1+=c1
            }else{
                k-=c2
                s2+=c2
            }
            return getKth(nums1,nums2,s1,s2,k)
        }
    }

    t_len=nums1.length+nums2.length
    if(t_len%2==0){
        var r1 = getKth(nums1,nums2,-1,-1,t_len/2)
        var r2 = getKth(nums1,nums2,-1,-1,t_len/2+1)
        return (r1+r2)/2.0
    }else{
        return getKth(nums1,nums2,-1,-1,Math.ceil(t_len/2.0))
    }

};
// @lc code=end

