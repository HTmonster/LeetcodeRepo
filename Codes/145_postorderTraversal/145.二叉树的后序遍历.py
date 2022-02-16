'''
Description: 
Autor: HTmonster
Date: 2022-02-16 21:24:04
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result,stack = [],[]

        prev=None
        while root or len(stack)> 0:
            # 1. 入栈自己及左节点直到没有
            while root:
                stack.append(root)
                root = root.left
            
            # a. 弹值
            root=stack.pop()

            # b. 如果没有右节点 或者节点写过
            if not root.right or root.right == prev:
                result.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root=root.right

        return result

# @lc code=end

