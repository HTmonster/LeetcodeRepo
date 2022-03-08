'''
Description: 
Autor: HTmonster
Date: 2022-02-20 19:54:40
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # preorder = [3*,9,| 20,15,7]
        # inorder =  [9,*3,| 15,20,7]
        # 退出条件
        if len(preorder)<=0: return None

        # 1.找到根节点，也就是pre中第一个
        rootVal=preorder[0]
        leftLen=-1 # 从in中寻找左子树的长度
        for i in range(len(inorder)):
            if inorder[i]==rootVal:
                leftLen=i
        root=TreeNode(rootVal)

        # 2. 建立左子树
        preLeft = preorder[1:1+leftLen]  # 拆分前序
        inLeft  = inorder[:leftLen]      # 拆分中序
        root.left = self.buildTree(preLeft,inLeft)

        # 3. 建立右子树
        preRight = preorder[1+leftLen:] # 拆分前序
        inRight   = inorder[leftLen+1:]  # 拆分中序
        root.right = self.buildTree(preRight,inRight)

        return root
        

# @lc code=end

