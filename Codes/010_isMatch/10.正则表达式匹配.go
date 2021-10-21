/*
 * @lc app=leetcode.cn id=10 lang=golang
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
func match(s string, p string, i int, j int) bool {
	if i == 0 {
		return false
	} else if p[j-1] == '.' {
		return true
	} else {
		return s[i-1] == p[j-1]
	}
}

func isMatch(s string, p string) bool {
	//1. re 作弊法
	// r, _ := regexp.MatchString("^"+p+"$", s)
	// return r
	//2 动态规划法
	// 存储数据
	var ds [][]bool

	for i := 0; i < (len(s) + 1); i++ {
		ds = append(ds, make([]bool, len(p)+1))

		ds[i][0] = false
		if i == 0 {
			ds[0][0] = true
		}
		for j := 1; j < (len(p) + 1); j++ {
			if p[j-1] == '*' {
				ds[i][j] = ds[i][j-2]
				if match(s, p, i, j-1) {
					ds[i][j] = ds[i-1][j] || ds[i][j]
				}
			} else {
				if match(s, p, i, j) {
					ds[i][j] = ds[i-1][j-1]
				} else {
					ds[i][j] = false
				}
			}
		}
	}

	return ds[len(s)][len(p)]

}

// @lc code=end

