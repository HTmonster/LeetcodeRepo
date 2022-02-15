'''
Description: 
Autor: HTmonster
Date: 2022-02-15 19:04:49
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newHead=None
        p=head

        while p !=None:
            temp=p
            p=p.next
            
            #转换链表
            temp.next=newHead
            newHead=temp

        return newHead
            
# @lc code=end

