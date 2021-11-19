/*
 * @lc app=leetcode.cn id=13 lang=golang
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
func romanToInt(s string) int {
	ROMANS := map[byte]int{'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

	last := ROMANS[s[0]]
	num := last
	for i := 1; i < len(s); i++ {
		now := ROMANS[s[i]]
		if now > last {
			now = now - 2*last
		}
		num += now
		last = now
	}

	return num

}

// @lc code=end

