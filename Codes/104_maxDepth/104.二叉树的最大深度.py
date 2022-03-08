'''
Description: 
Autor: HTmonster
Date: 2022-02-20 19:47:16
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归方法
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 递归方程为 D(n)=1+max(D(n.left),D(n.right))
        if root is None: return 0   # 退出条件
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
# @lc code=end

