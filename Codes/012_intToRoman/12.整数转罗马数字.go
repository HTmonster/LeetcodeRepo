/*
 * @lc app=leetcode.cn id=12 lang=golang
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
func intToRoman(num int) string {
	I := [10]string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
	X := [10]string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
	C := [10]string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
	M := [10]string{"", "M", "MM", "MMM"}
	ALL := [...][10]string{I, X, C, M}

	roman := ""
	for i := 0; i < 4; i++ {
		roman = ALL[i][num%10] + roman
		num /= 10
	}

	return roman

}

// @lc code=end

