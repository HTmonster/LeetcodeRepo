<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-02-17 09:59:24
-->

## 链表

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|19.删除链表的倒数第 N 个结点| 给你一个链表，删除链表的倒数第n个结点，并且返回链表的头结点|1.入栈法 2.双指针法 ![](http://latex.codecogs.com/gif.latex?O(1)\,O(1))||
|206.反转链表|给你单链表的头节点`head`，请你反转链表，并返回反转后的链表|1.双指针修改法![](http://latex.codecogs.com/gif.latex?O(n)\,O(1)) 2.递归法  |注意原有的head变成tail后next要指向空, golang 注意nil类型的定义|