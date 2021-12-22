/*
 * @lc app=leetcode.cn id=16 lang=golang
 *
 * [16] 最接近的三数之和
 */

// @lc code=start
func threeSumClosest(nums []int, target int) int {
	almost := math.MinInt64

	//0.排序
	sort.Ints(nums)
	//1.单遍历+双指针
	for i := 0; i < len(nums)-1; i++ {
		left := i + 1
		right := len(nums) - 1
		for {
			if left >= right {
				break
			}
			sum := nums[i] + nums[left] + nums[right]

			if sum > target {
				right--
			} else if sum == target {
				return target
			} else {
				left++
			}

			if math.Abs(float64(sum-target)) < math.Abs(float64(almost-target)) {
				almost = sum
			}
		}
	}

	return almost
}

// @lc code=end
