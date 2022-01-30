'''
Description: 
Autor: HTmonster
Date: 2022-01-30 09:49:51
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 多指针并行遍历
        toRemove_left=toRemove=tail=head

        # 遍历
        count=0
        while tail!=None:
            if count>n:
                toRemove_left=toRemove_left.next
            if count>=n:
                toRemove=toRemove.next
            tail=tail.next
            count+=1
        # print(toRemove_left.val)
        # print(toRemove.val)
        # print(tail)
        # 移除
        # 特殊情况
        if toRemove==head:
            head=head.next
        # 一般情况
        else:
            toRemove_left.next=toRemove.next
        del toRemove

        return head
                
                
# @lc code=end

