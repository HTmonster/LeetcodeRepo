/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-20 19:18:03
 */
/*
 * @lc app=leetcode.cn id=102 lang=golang
 *
 * [102] 二叉树的层序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	queue := make([]*TreeNode, 0)
	ans := make([][]int, 0)

	// 添加第一个需要处理的二数据
	if root != nil {
		queue = append(queue, root)
	}

	// 当队列还有数据时候进行处理
	for len(queue) > 0 {
		layer := make([]int, 0)      // 本层的值
		next := make([]*TreeNode, 0) // 下一层要遍历的值

		for i := range queue {
			node := queue[i]                //要处理的节点
			layer = append(layer, node.Val) // 添加值

			// 不为空时候 添加节点
			if node.Left != nil {
				next = append(next, node.Left)
			}
			if node.Right != nil {
				next = append(next, node.Right)
			}
		}
		// 添加本层数据
		ans = append(ans, layer)
		// 处理下一层
		queue = next
	}

	return ans

}

// @lc code=end

