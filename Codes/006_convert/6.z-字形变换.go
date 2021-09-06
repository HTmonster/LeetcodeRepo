/*
 * @Author: Theo_hui
 * @Date: 2021-09-06 10:37:49
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=6 lang=golang
 *
 * [6] Z 字形变换
 */

// @lc code=start
func convert(s string, numRows int) string {

	// 特殊情况
	if numRows == 1 {
		return s
	}

	//转换填充器
	storage := make([][]rune, numRows)

	line, flag := 0, 1

	// 转换填充
	for _, c := range s {
		storage[line] = append(storage[line], c)
		if (flag == 1 && line == numRows-1) || (flag == -1 && line == 0) {
			flag = -flag
		}
		line = line + flag
	}

	// 读取拼接
	rst_list := []rune{}
	for i := 0; i < numRows; i++ {
		rst_list = append(rst_list, storage[i]...)
	}

	return string(rst_list)

}

// @lc code=end

