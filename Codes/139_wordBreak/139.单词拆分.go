/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-03-22 10:42:37
 */
/*
 * @lc app=leetcode.cn id=139 lang=golang
 *
 * [139] 单词拆分
 */

// @lc code=start
func wordBreak(s string, wordDict []string) bool {

	// 备忘录
	mem := make(map[int]bool) //位置:是否能解决

	var subfunc func(int) bool //子函数
	subfunc = func(idx int) bool {
		// 退出条件
		if idx > len(s)-1 {
			return true
		}
		// 查备忘录 存在则直接返回结果
		if r, ok := mem[idx]; ok {
			return r
		}

		// 遍历字典
		flag := false
		for i := range wordDict {
			if strings.HasPrefix(s[idx:], wordDict[i]) {
				flag = flag || subfunc(idx+len(wordDict[i]))
				if flag {
					break
				}
			}
		}
		// 添加备忘录
		mem[idx] = flag

		return flag
	}

	return subfunc(0)

}

// @lc code=end

