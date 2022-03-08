'''
Description: 
Autor: HTmonster
Date: 2022-02-20 19:30:58
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue=[]
        ans=[]
        flag=True  #t:左->右 f:右->左

        if root: queue.append(root)

        # 处理数据
        while len(queue)>0:
            layerVal  = []  #本层的值
            nextLayer = []  #下层的节点
            
            for node in queue:
                if flag:
                    layerVal.append(node.val) # 记录值
                else:
                    layerVal.insert(0,node.val)
                # 添加下层数据   根据标志决定添加位置
                if node.left: 
                        nextLayer.append(node.left)
                if node.right: 
                        nextLayer.append(node.right)
            # 记录本次
            ans.append(layerVal)
            queue=nextLayer
            flag= not flag    #反转标志
        
        return ans
                
# @lc code=end

