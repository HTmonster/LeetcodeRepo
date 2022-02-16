'''
Description: 
Autor: HTmonster
Date: 2022-02-16 19:55:34
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
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
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     result=[]
    #     def dfs(node):
    #         if not node: return       # 退出条件
    #         nonlocal result
    #         result.append(node.val)   # 1.保存根节点

    #         dfs(node.left)            # 2.遍历左节点
    #         dfs(node.right)           # 3.遍历右节点

    #     dfs(root)
    #     return result

    # 迭代法
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack,result=[],[]
        
        if root: stack.append(root)             # 根节点首先入站
        while len(stack) > 0:
            node=stack.pop()                    # 1弹出第一个
            result.append(node.val)             # 添加值

            if node.right:
                stack.append(node.right)        # 2加右子树
            
            if node.left:
                stack.append(node.left)         # 3加左子树

        return result
# @lc code=end

