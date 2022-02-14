/*
 * @Description:
 * @Autor: HTmonster
 * @Date: 2022-02-14 20:09:27
 */
/*
 * @lc app=leetcode.cn id=146 lang=golang
 *
 * [146] LRU 缓存
 */

// @lc code=start
type Node struct {
	Key   int
	Value int
	Prev  *Node
	Next  *Node
}

type LRUCache struct {
	DlinkHead *Node
	HashTable map[int]*Node
	Capacity  int
}

func Constructor(capacity int) LRUCache {
	// 创建双向链表
	head := Node{
		Key:   0,
		Value: 0,
	}
	tail := Node{
		Key:   0,
		Value: 0,
	}
	head.Next = &tail
	head.Prev = &tail
	tail.Next = &head
	tail.Prev = &head

	// 返回结构体
	return LRUCache{
		DlinkHead: &head,
		HashTable: make(map[int]*Node),
		Capacity:  capacity,
	}
}

func insertHead(head, node *Node) {
	//将节点插入链表的头部
	node.Next = head.Next
	head.Next.Prev = node
	head.Next = node
	node.Prev = head
}

func peakNode(node *Node) *Node {
	//摘出节点
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
	return node
}

// func printLink(head *Node) {
// 	p := head
// 	for {
// 		if p.Next == head {
// 			break
// 		}
// 		fmt.Printf("%d-->", p.Key)
// 		p = p.Next
// 	}
// 	fmt.Printf("\n")
// }

func (this *LRUCache) Get(key int) int {
	fmt.Printf("get %d\n", key)
	// 检查是否存在
	node, ok := this.HashTable[key]
	// 不存在返回-1
	if !ok {
		// printLink(this.DlinkHead)
		return -1
	} else {
		// 存在
		// 摘出该节点
		node = peakNode(node)
		// 放到头部
		insertHead(this.DlinkHead, node)
		// printLink(this.DlinkHead)
		return node.Value
	}

}

func (this *LRUCache) Put(key int, value int) {
	fmt.Printf("put %d %d\n", key, value)
	//0.先检查是否存在
	node, ok := this.HashTable[key]
	if ok {
		//0.a 存在
		// 改值
		node.Value = value
		// 摘出节点
		node = peakNode(node)
	} else {
		//0.b 不存在
		// 创建节点
		node = &Node{
			Key:   key,
			Value: value,
		}
	}
	// 将节点插入头部
	insertHead(this.DlinkHead, node)
	// 存入hash表
	this.HashTable[key] = node
	// 检查并删除多余的元素
	fmt.Printf("%d!!!\n", len(this.HashTable))
	if len(this.HashTable) > this.Capacity {
		last := this.DlinkHead.Prev.Prev

		// 摘出节点
		last = peakNode(last)

		// 删除hash表
		delete(this.HashTable, last.Key)
		// 删除链表（自动）
	}
	// printLink(this.DlinkHead)
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end

