'''
Description: 
Autor: HTmonster
Date: 2022-02-16 20:39:45
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归法
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result = []

    #     def traversal(node):
    #         nonlocal result

    #         if not node:                        # 退出条件
    #             return
    #         traversal(node.left)                # 1. 遍历左子树
    #         result.append(node.val)             # 2. 写值
    #         traversal(node.right)               # 3. 遍历右子树
        
    #     traversal(root) 
    #     return result 
    
    # 迭代法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,result = [],[]

        #当栈不为空时
        while root or len(stack)>0:
            #1. 一直添加左结点（包括自己）
            while root:
                stack.append(root)
                root=root.left
            
            #2. 直到没有左节点
            # a. 弹出栈
            root=stack.pop()
            # b. 写
            result.append(root.val)
            # c. 转到右节点
            root=root.right
        
        return result
# @lc code=end

