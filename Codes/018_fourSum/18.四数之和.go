/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-01-25 11:54:01
 */
/*
 * @lc app=leetcode.cn id=18 lang=golang
 *
 * [18] 四数之和
 */

// @lc code=start
func fourSum(nums []int, target int) [][]int {

	// 排序
	sort.Ints(nums)
	var result [][]int

	/* i */
	for i := 0; i < len(nums)-3; i++ {
		// i去重
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		/* j */
		for j := i + 1; j < len(nums)-2; j++ {
			// j 去重
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			m := j + 1
			n := len(nums) - 1
			for {
				if m >= n {
					break
				}
				sum := nums[i] + nums[j] + nums[m] + nums[n]

				if sum > target {
					n--
				} else if sum < target {
					m++
				} else {
					result = append(result, []int{nums[i], nums[j], nums[m], nums[n]})
					n--
					m++
					for {
						if n <= m || nums[n] != nums[n+1] {
							break
						}
						n--
					}
					for {
						if n <= m || nums[m] != nums[m-1] {
							break
						}
						m++
					}
				}
			}

		}
	}
	return result

}

// @lc code=end

