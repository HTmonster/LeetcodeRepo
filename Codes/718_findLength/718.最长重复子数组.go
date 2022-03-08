/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-17 15:16:41
 */
/*
 * @lc app=leetcode.cn id=718 lang=golang
 *
 * [718] 最长重复子数组
 */

// @lc code=start
func findLength(A []int, B []int) int {
	n, m := len(A), len(B)
	dp := make([][]int, n+1)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, m+1)
	}
	ans := 0
	for i := 0; i < len(A); i++ {
		for j := 0; j < len(B); j++ {
			if A[i] == B[j] {
				dp[i+1][j+1] = dp[i][j] + 1
			} else {
				dp[i+1][j+1] = 0
			}
			if ans < dp[i+1][j+1] {
				ans = dp[i+1][j+1]
			}
		}
	}
	return ans

}

// @lc code=end

