/*
 * @Author: Theo_hui
 * @Date: 2021-08-27 16:25:31
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=5 lang=golang
 *
 * [5] 最长回文子串
 */

// @lc code=start

func expend(s string, left, right int) (int, int) {
	for {
		if left >= 0 && right < len(s) && s[left] == s[right] {
			left--
			right++
		} else {
			break
		}
	}
	return left + 1, right - 1
}

func longestPalindrome(s string) string {
	//中心拓展法

	//记录最值情况
	best_r, best_l := 0, 0

	//遍历
	for i, _ := range s {
		l1, r1 := expend(s, i, i)
		l2, r2 := expend(s, i, i+1)

		var r, l int

		if (r1 - l1) > (r2 - l2) {
			r, l = r1, l1
		} else {
			r, l = r2, l2
		}

		if (r - l) > (best_r - best_l) {
			best_l, best_r = l, r
		}
	}

	return s[best_l : best_r+1]

}

// @lc code=end

