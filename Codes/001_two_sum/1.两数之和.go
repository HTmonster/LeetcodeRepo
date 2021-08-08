/*
 * @Author: Theo_hui
 * @Date: 2021-08-08 19:30:55
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

/*
	1.粗暴遍历法
*/
// @lc code=start
// func twoSum(nums []int, target int) []int {
// 	// 双下标
// 	index1, index2 := 0, 0
// 	for i := 0; i < len(nums)-1; i++ {
// 		for j := i + 1; j < len(nums); j++ {
// 			if nums[i]+nums[j] == target {
// 				index1, index2 = i, j
// 			}
// 		}
// 	}

// 	return []int{index1, index2}

// }

/*
	2.哈希法
*/
// @lc code=start
func twoSum(nums []int, target int) []int {
	//1. 创建哈希表
	hashT := map[int]int{}

	for i, v := range nums {
		if j, ok := hashT[target-v]; ok {
			return []int{i, j}
		}
		hashT[v] = i
	}

	return []int{}
}

// @lc code=end
