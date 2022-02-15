/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-15 19:29:00
 */
/*
 * @lc app=leetcode.cn id=206 lang=golang
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	var newHead *ListNode = nil
	p := head

	for nil != p {
		temp := p.Next
		//反转链表
		p.Next = newHead
		newHead = p

		p = temp
	}

	return newHead

}

// @lc code=end

