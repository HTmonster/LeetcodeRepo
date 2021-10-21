/*
 * @lc app=leetcode.cn id=9 lang=golang
 *
 * [9] 回文数
 */

// @lc code=start
func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	str_x := strconv.Itoa(x)
	i := 0
	j := len(str_x) - 1
	for {
		if str_x[i] != str_x[j] {
			return false
		}
		i++
		j--
		if i > j {
			return true
		}
	}

}

// @lc code=end

