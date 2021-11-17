/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
func maxArea(height []int) int {

	left := 0
	right := len(height) - 1
	maxValue := -1

	for {
		if  {
			break
		}

		value_left := height[left]
		value_right := height[right]

		var value int
		if value_left > value_right {
			value = (right - left) * value_right
			for ; height[right] <= value_right && right > left; right-- {
			}
		} else {
			value = (right - left) * value_left
			for ; height[left] <= value_left && right > left; left++ {
			}
		}

		if value > maxValue {
			maxValue = value
		}
	}

	return maxValue

}

// @lc code=end

