/*
 * @Author: Theo_hui
 * @Date: 2021-09-08 19:54:52
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=8 lang=golang
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
func myAtoi(s string) int {

	rst, symbol := 0, 1

	i, status := 0, 0
	for {
		if i >= len(s) {
			break
		}
		//取字符
		c := s[i]

		//状态0：处理空格
		if status == 0 {
			if c == ' ' {
				i++
			} else {
				status = 1
			}
			//状态1：处理符号
		} else if status == 1 {
			if c == '+' {
				i++
			} else if c == '-' {
				symbol = -1
				i++
			}
			status = 2
			//状态2：处理数字
		} else if status == 2 {
			if c <= '9' && c >= '0' {
				rst = rst*10 + (int)(c-'0')
				if symbol == 1 && rst > math.MaxInt32 {
					rst = math.MaxInt32
					break
				}
				if symbol == -1 && rst > math.MaxInt32+1 {
					rst = math.MaxInt32 + 1
					break
				}
				i++
			} else {
				break
			}
		}
	}

	return rst * symbol
}

// @lc code=end

