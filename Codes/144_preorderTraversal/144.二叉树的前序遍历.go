/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-16 20:09:38
 */
/*
 * @lc app=leetcode.cn id=144 lang=golang
 *
 * [144] 二叉树的前序遍历
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
// 递归法
// func preorderTraversal(root *TreeNode) (result []int) {
// 	var dfs func(*TreeNode)

// 	dfs = func(node *TreeNode) { //递归函数
// 		if node == nil {
// 			return //退出条件
// 		}
// 		result = append(result, node.Val) //1. 记录本节点
// 		dfs(node.Left)                    //2. 遍历左节点
// 		dfs(node.Right)                   //3. 遍历右节点
// 	}

// 	dfs(root)
// 	return
// }
func preorderTraversal(root *TreeNode) (result []int) {
	stack := make([]*TreeNode, 0)

	if root == nil {
		return
	}
	stack = append(stack, root) // 入根节点

	for len(stack) > 0 {
		node := stack[len(stack)-1] //1. 弹出
		stack = stack[:len(stack)-1]

		result = append(result, node.Val) //2. 记录
		if node.Right != nil {
			stack = append(stack, node.Right) //3.入栈右子树
		}
		if node.Left != nil {
			stack = append(stack, node.Left) //4.入栈左子树
		}
	}
	return
}

// @lc code=end

