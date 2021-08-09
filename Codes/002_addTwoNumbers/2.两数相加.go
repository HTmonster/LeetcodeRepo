/*
 * @Author: Theo_hui
 * @Date: 2021-08-09 09:30:11
 * @Descripttion:
 */
/*
 * @lc app=leetcode.cn id=2 lang=golang
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// 模拟进位法
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	var head, tail *ListNode //头部节点 尾部节点
	c := 0                   //进位

	for l1 != nil || l2 != nil {
		var a, b int

		if l1 != nil {
			a = l1.Val
			l1 = l1.Next
		} else {
			a = 0
		}

		if l2 != nil {
			b = l2.Val
			l2 = l2.Next
		} else {
			b = 0
		}

		sum := a + b + c //相加
		c = sum / 10
		temp := &ListNode{Val: sum % 10} //新节点

		if head == nil {
			head = temp
		} else {
			tail.Next = temp
		}
		tail = temp
	}

	if c > 0 {
		tail.Next = &ListNode{Val: c}
	}

	return head
}

// @lc code=end

