/*
 * @Author: Theo_hui
 * @Date: 2021-08-17 10:45:55
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=3 lang=golang
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	res, left := 0, -1           //结果，左下标
	c_maps := make(map[rune]int) // 字符最右下标字典

	for right, c := range s {
		i, ok := c_maps[c] //该字符的最右下标

		if ok && i > left {
			//字符重复了
			left = i
		} else {
			//没有重复，更新结果
			new_res := right - left
			if new_res > res {
				res = new_res
			}
		}
		// 更新字符最右位置
		c_maps[c] = right
	}
	return res
}

// @lc code=end

