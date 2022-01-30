/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-01-30 10:33:24
 */
/*
 * @lc app=leetcode.cn id=19 lang=golang
 *
 * [19] 删除链表的倒数第 N 个结点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// 三指针
	left := head
	toRemove := head
	tail := head

	// 单次遍历
	count := 0
	for {
		if tail == nil {
			break
		}
		if count > n {
			left = left.Next
		}
		if count >= n {
			toRemove = toRemove.Next
		}
		tail = tail.Next
		count++
	}

	// 特殊情况
	if toRemove == head {
		head = head.Next
	} else {
		left.Next = toRemove.Next
	}
	// 自动回收
	toRemove = nil

	return head
}

// @lc code=end

