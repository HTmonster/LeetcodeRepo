'''
Description: 
Autor: HTmonster
Date: 2022-02-20 21:24:27
'''
#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
from distutils.command.build import build


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #层次遍历
        queue=[]
        ans=[]

        if root:queue.append(root)

        while len(queue)>0:
            next=[]
            for node in queue:
                if not node:
                    ans.append("null")
                else:
                    ans.append(str(node.val))
                    next.append(node.left)
                    next.append(node.right)
            queue=next
        ans=str(ans)

        return ans
                   
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes=[x.strip()[1:-1] for x in data[1:-1].split(",")]

        if len(nodes)==1 and nodes[0]=='':
            return None

        root=TreeNode(int(nodes[0]))
        queue =collections.deque([root])
        i=1
        while queue:
            node = queue.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i+=1
            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i+=1
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

