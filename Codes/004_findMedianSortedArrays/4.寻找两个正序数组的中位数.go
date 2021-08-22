/*
 * @Author: Theo_hui
 * @Date: 2021-08-22 16:24:41
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=4 lang=golang
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
//判断最小值
func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

// 递归函数 第k小的数 二分查找法
func getKth(nums1, nums2 []int, s1, s2, k int) int {

	// 每部分的区间长度
	len1, len2 := len(nums1)-1-s1, len(nums2)-1-s2
	// 递归出口 一些特殊情况
	//1.其中一个数组分空
	if len1 == 0 {
		return nums2[s2+k]
	}
	if len2 == 0 {
		return nums1[s1+k]
	}
	//2.k为1
	if k == 1 {
		return Min(nums1[s1+1], nums2[s2+1])
	} else {
		midk := int(k / 2)
		//两个数组的排除区间
		c1 := Min(len1, midk)
		c2 := Min(len2, midk)
		//排除小的一部分
		if nums1[s1+c1] < nums2[s2+c2] {
			k -= c1
			s1 += c1
		} else {
			k -= c2
			s2 += c2
		}
		//递归调用
		return getKth(nums1, nums2, s1, s2, k)
	}
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {

	//获得k
	t_len := len(nums1) + len(nums2)
	if t_len%2 == 0 {
		//偶数
		r1 := getKth(nums1, nums2, -1, -1, int(t_len/2))
		r2 := getKth(nums1, nums2, -1, -1, int(t_len/2)+1)
		return float64(r1+r2) / 2.0
	} else {
		return float64((getKth(nums1, nums2, -1, -1, int(t_len/2)+1)))
	}
}

// @lc code=end

