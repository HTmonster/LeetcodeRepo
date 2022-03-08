'''
Description: 
Autor: HTmonster
Date: 2022-02-20 21:02:38
'''
#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 先序遍历
        queue=[]
        if root: 
            queue.append(root)
    
        # 先序遍历方法
        tail=None   # 链表的尾部
        while len(queue)>0:
            # 1. 弹出一个
            node=queue.pop()
            # 2. 先添加左右节点
            if node.right:queue.append(node.right)
            if node.left:queue.append(node.left)
            # 3. 把该节点加入链表
            node.left=None
            if tail:tail.right=node
            tail=node
                

# @lc code=end

