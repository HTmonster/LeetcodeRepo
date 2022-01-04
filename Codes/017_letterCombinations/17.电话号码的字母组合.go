/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		rst := []string{}
		return rst
	}

	num2char := [][]byte{
		{'a', 'b', 'c'},
		{'d', 'e', 'f'},
		{'g', 'h', 'i'},
		{'j', 'k', 'l'},
		{'m', 'n', 'o'},
		{'p', 'q', 'r', 's'},
		{'t', 'u', 'v'},
		{'w', 'x', 'y', 'z'},
	}

	rst := []string{""}
	for i := 0; i < len(digits); i++ {
		num := digits[i] - '2'
		var copy []string
		for _, value := range rst {
			for j := 0; j < len(num2char[num]); j++ {
				//fmt.Println(value + string(num2char[num][j]))
				copy = append(copy, value+string(num2char[num][j]))
			}
		}
		rst = copy
	}

	return rst
}

// @lc code=end

