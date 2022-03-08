'''
Description: 
Autor: HTmonster
Date: 2022-02-20 18:39:05
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if p==None and q==None:      # 退出条件
    #         return True
    #     if p==None or q==None: 
    #         return False
    #     if p.val != q.val:
    #         return False
    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack_p,stack_q=[],[]
        
        # 使用中序遍历的方法
        stack_p.append(p)
        stack_q.append(q)

        # 一一对比，一旦对比到不符合就退出
        while len(stack_q)>0 and len(stack_p)>0:
            i,j=stack_q.pop(),stack_p.pop() #1. 弹栈
            
            # 对比相同，相同的条件： 值相同 且左右节点结构相同
            if i==None or j==None:
                if i!=j:
                    return False
                else:
                    continue
            if (i.left==None or j.left==None) and i.left !=j.left:
                return False
            if (i.right==None or j.right==None) and i.right !=j.right:
                return False
            if i.val !=j.val:
                return False
            # 入栈
            stack_q.append(i.left)
            stack_q.append(i.right)
            stack_p.append(j.left)
            stack_p.append(j.right)

        return True
# @lc code=end

