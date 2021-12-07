/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	var rst [][]int
	n := len(nums)

	if n < 3 {
		return rst
	}

	//排序
	sort.Ints(nums)

	//单遍历+双指针夹逼匹配
	for i := 0; i < n; i++ {
		// 去除重复数 避免重复结果
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		// 没有结果了
		if nums[i] > 0 {
			break
		}
		L := i + 1
		R := n - 1
		for L < R {
			sum := nums[i] + nums[L] + nums[R]
			if sum == 0 {
				rst = append(rst, []int{nums[i], nums[L], nums[R]})
				for {
					if L < R && nums[L+1] == nums[L] {
						L++
					} else {
						break
					}

				}
				for {
					if L < R && nums[R-1] == nums[R] {
						R--
					} else {
						break
					}
				}
				L++
				R--
			} else if sum < 0 {
				L++
			} else {
				R--
			}
		}
	}

	return rst
}

// @lc code=end

