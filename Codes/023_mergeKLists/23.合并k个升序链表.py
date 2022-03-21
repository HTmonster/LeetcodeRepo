'''
Description: 
Autor: HTmonster
Date: 2022-03-21 19:02:25
'''
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Heap:
    
    # 存储结构为数组
    L=None

    def __init__(self):
        self.L=[]

    # 比较的标准 大于
    def greater(self, i,j):
        return self.L[i].val>self.L[j].val
    
    # 上浮
    def up(self,i):
        # 其父节点
        while i>0:
            p=(i-1)//2 # 父亲节点
            
            # 当父节点大于子节点
            if self.greater(p,i):
                # 交换节点
                self.L[p],self.L[i]=self.L[i],self.L[p]
                # 接着处理
                i=p
            else:
                return
    # 下沉
    def down(self,i):
        while i<len(self.L):
            lc,rc=2*i+1,2*i+2 #左孩子与右孩子
            minc,minval=None,float("inf")
            # 找到最小孩子的值
            if lc<len(self.L):
                minc=lc
                minval=self.L[lc].val
            if rc<len(self.L) and minval>self.L[rc].val:
                minc=rc
            
            # 如果大于孩子，与最小的孩子进行交换
            if minc and self.greater(i,minc):
                self.L[i],self.L[minc]=self.L[minc],self.L[i]
                i=minc
            else:
                return
            # print(i,rc,lc,minc)
            # print([x.val for x in self.L])

    # 插入
    def push(self,item):
        self.L.append(item)      #插入
        self.up(len(self.L)-1)   #上浮



    # 弹出
    def pop(self):
        head=self.L[0]
        tail=self.L.pop()

        if len(self.L):
            self.L[0]=tail
            self.down(0)

        return head
    
    def empty(self):
        return not len(self.L)







class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap=Heap()
        
        # 存进最小堆
        for l in lists:
            while l:
                heap.push(l)
                l=l.next
        
        if heap.empty():
            return None
        # 取出最小堆
        node=heap.pop()
        root,tail=node,node
        while not heap.empty():
            node=heap.pop()
            tail.next=node
            tail=node
        tail.next=None

        return root
        
        
        
# @lc code=end

