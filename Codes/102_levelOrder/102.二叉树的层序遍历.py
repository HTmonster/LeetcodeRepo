'''
Description: 
Autor: HTmonster
Date: 2022-02-20 19:05:48
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 使用队列辅助
        queue=[] # 本次
        ans=[]

        if root:
            queue.append(root)

        while len(queue) > 0:
            layer,queueNext=[],[]
            # 遍历本层次的节点
            for node in queue:
                layer.append(node.val) # 记录值
                if node.left: queueNext.append(node.left)
                if node.right: queueNext.append(node.right)

            ans.append(layer)
            queue=queueNext
        
        return ans

        
# @lc code=end

