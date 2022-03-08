/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-18 15:09:05
 */
/*
 * @lc app=leetcode.cn id=76 lang=golang
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
func minWindow(s string, t string) string {

	// 先建立一个字符的索引，以及需求的数组
	tIndex := make(map[byte]int)
	need := make([]int, 0) // 目标需要的计数
	cnt := make([]int, 0)  // 已经包含的计数

	i := 0
	for j := 0; j < len(t); j++ {
		c := t[j]
		//已经包含了 例如 "aa"
		if _, ok := tIndex[c]; ok {
			need[tIndex[c]]++
		} else {
			tIndex[c] = i
			need = append(need, 1)
			cnt = append(cnt, 0)
			i++
		}
	}

	fmt.Println(tIndex, need)

	// 检查函数 检查是否满足要求
	var check func() bool
	check = func() bool {
		for i := range need {
			// 其中一项还没达到要求
			if need[i] > cnt[i] {
				return false
			}
		}
		return true
	}

	ansLeft, ansRight := 0, math.MaxInt32 // 答案的范围
	left, right := 0, 0                   // 窗口

	for right < len(s) {
		//1. 窗口扩大
		for !check() && right < len(s) {
			// 包含了一个字符
			if index, ok := tIndex[s[right]]; ok {
				cnt[index]++
			}
			right++
		}
		// fmt.Println(left, right, s[left:right], cnt)

		//2.窗口缩小
		for check() && left < right {
			//更新值
			if right-left < ansRight-ansLeft {
				ansLeft = left
				ansRight = right
			}

			// 去除一个字符
			if index, ok := tIndex[s[left]]; ok {
				cnt[index]--
			}
			left++
			// fmt.Println("*", left, right, s[left:right], cnt)
		}
	}

	if ansRight == math.MaxInt32 {
		return ""
	} else {
		return s[ansLeft:ansRight]
	}
}

// @lc code=end

