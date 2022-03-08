'''
Description: 
Autor: HTmonster
Date: 2022-02-17 10:11:06
'''
#
# @lc app=leetcode.cn id=1382 lang=python3
#
# [1382] 将二叉搜索树变平衡
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder=[]

        # 中序遍历
        def dfs(root):
            nonlocal inorder
            if root==None:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        # 中间拆分建立
        def build(list):
            if len(list)<=0:
                return None
            # 中间拆分
            mid = int(len(list)/2)
            # 建立中间节点
            node = TreeNode(list[mid])
            # 递归构建左子树
            
            node.left =build(list[:mid])
            # 递归构建右子树
            node.right = build(list[mid+1:])
            return node

        # 1. 中序遍历得到有序数组
        dfs(root)
        # 2. 根据有序数组构建树
        return build(inorder)
        
# @lc code=end

