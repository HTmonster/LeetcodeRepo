'''
Author: Theo_hui
Date: 2021-08-09 10:32:30
Descripttion: 
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ## 模拟进位法
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head=tail = None  # 首尾节点

        carry = 0         # 进位
        while l1 or l2:
            a=b=0
            if l1:
                a=l1.val
                l1=l1.next
            if l2:
                b=l2.val
                l2=l2.next

            sum = a+b+carry  #相加值
            temp = ListNode(sum%10)
            carry = sum //10
            
            if tail:
                tail.next=temp
                tail=temp
            else:
                head=tail=temp
        
        if carry>0:
            tail.next=ListNode(carry)
        
        return head

# @lc code=end

