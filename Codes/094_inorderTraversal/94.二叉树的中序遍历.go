/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-16 21:07:37
 */
/*
 * @lc app=leetcode.cn id=94 lang=golang
 *
 * [94] 二叉树的中序遍历
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
// func inorderTraversal(root *TreeNode) (result []int) {
// 	var traversal func(*TreeNode)

// 	traversal = func(node *TreeNode) {
// 		if node == nil {
// 			return
// 		}
// 		traversal(node.Left)
// 		result = append(result, node.Val)
// 		traversal(node.Right)
// 	}

// 	traversal(root)
// 	return
// }
func inorderTraversal(root *TreeNode) (result []int) {
	stack := make([]*TreeNode, 0)

	for root != nil || len(stack) > 0 {

		//1. 入栈自己及左节点直至没有
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		//a. 出栈
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		//b. 写
		result = append(result, root.Val)

		//c. 转到右节点
		root = root.Right
	}

	return
}

// @lc code=end

