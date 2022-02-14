'''
Description: 
Autor: HTmonster
Date: 2022-02-14 19:07:34
'''
#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class Node:

    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next=None


class LRUCache:
    # 两大数据结构
    #a. 双向链表  (用于保存顺序)
    DoubleLinkedList = None
    #b. hashtable (用于快速存取值)
    HashMap = None

    def printLink(self):
        print(self.HashMap)
        p=self.DoubleLinkedList
        while p.key!="tail":
            print("{}-->".format(p.key),end='')
            p=p.next
        print("tail")

    def __init__(self, capacity: int):
        # 初始化数据结构
        self.initDoubleLinkedList()
        self.capacity = capacity
        self.HashMap = {}
    
    def initDoubleLinkedList(self):
        head = Node(key="head")
        tail = Node(key="tail")
        head.next=tail
        head.prev=tail
        tail.next=head
        tail.prev=head
        self.DoubleLinkedList=head

        # self.printLink()

    def get(self, key: int) -> int:
        # print("get",key)
        # hash表中检查是否存在
        if key in self.HashMap.keys():
            # 挑战位置
            getNode = self.HashMap[key]
            # 摘出
            getNode.prev.next=getNode.next
            getNode.next.prev=getNode.prev
            
            # 插入头部
            self.insertHead(getNode)
            # self.printLink()
            return getNode.value
        else:
            # self.printLink()
            return -1

    def put(self, key: int, value: int) -> None:
        # print("put",key,value)
        #1. 先查找hash map
        if key in self.HashMap.keys():
            #2. 存在则修改值
            self.HashMap[key].value=value
            self.get(key)
        else:
            #3. 不存在则创建
            self.addNode(key, value)
        self.checkAndDelete()
        # self.printLink()
    
    def checkAndDelete(self):
        # 检查并删除多余的元素
        if len(self.HashMap.keys())>self.capacity:
            # 取出最后一个节点
            last_node=self.DoubleLinkedList.prev.prev
            # 删除hash表中的数据
            del self.HashMap[last_node.key]
            # 删除链表中的数据
            last_node.prev.next=last_node.next
            last_node.next.prev=last_node.prev
            del last_node
    
    def addNode(self,key,value):
        # 添加一个新节点
        node= Node(key=key,value=value)
        self.HashMap[key]=node
        self.insertHead(node)


    def insertHead(self,node):
        # 插入链表的头部
        node.next=self.DoubleLinkedList.next
        self.DoubleLinkedList.next.prev=node
        self.DoubleLinkedList.next=node
        node.prev=self.DoubleLinkedList

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
