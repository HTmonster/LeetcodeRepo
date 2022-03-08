/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-20 20:26:21
 */
/*
 * @lc app=leetcode.cn id=106 lang=golang
 *
 * [106] 从中序与后序遍历序列构造二叉树
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
func buildTree(inorder []int, postorder []int) *TreeNode {
	// inorder =   [9,|*3, 15,20, 7]
	// postorder = [9,|15, 7,20,*3]
	// [15,|*20, 7]
	// [15,| 7,20*]

	// 建立中序遍历索引表
	inIndex := make(map[int]int)
	for i := range inorder {
		inIndex[inorder[i]] = i //值:位置
	}
	// fmt.Println(inIndex)

	// 递归函数
	var myBuildTree func(int, int, int, int) *TreeNode
	myBuildTree = func(inLeft, inRight, postLeft, postRight int) *TreeNode {
		// fmt.Println(inLeft, inRight, postLeft, postRight)
		//退出条件
		if inLeft >= inRight {
			return nil
		}

		//1. 取出根节点
		rootVal := postorder[postRight-1]
		rootIndex := inIndex[rootVal] //根节点在中序的位置
		leftLen := rootIndex - inLeft //左子树长度

		//2. 建立左子树
		left := myBuildTree(inLeft, inLeft+leftLen, postLeft, postLeft+leftLen)

		//3. 建立右子树
		right := myBuildTree(inLeft+leftLen+1, inRight, postLeft+leftLen, postRight-1)

		//4. 建立节点
		return &TreeNode{
			Val:   rootVal,
			Left:  left,
			Right: right,
		}
	}

	return myBuildTree(0, len(inorder), 0, len(postorder))
}

// @lc code=end

