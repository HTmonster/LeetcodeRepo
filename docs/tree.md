<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-02-17 10:00:22
-->


## 树

### 二叉树

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|144. 二叉树的前序遍历| 1.递归法 *根-dg(左树)-dg(右树) 2. 迭代法 栈不为空时 1.入栈自己  a.弹 b.写 c.入**右** d.入左 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))||
|94.  二叉树的中序遍历| 1.递归法 *dg(左树)-根-dg(右树) 2. 迭代法 栈不为空时 1.入栈自己及左直到没有 a.弹 b.写 c.转到右 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))||
|145. 二叉树的后序遍历| 1.递归法 dg(左树)-dg(右树)-*根 2. 迭代法 栈不为空时 1.入栈自己及左直到没有 a.弹 b.(如果没有右节点或右节点写过)写 c.否则入栈自己且转到右  ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))||
|100. 相同的数|1.递归法 `same[p,q]=same[p.l,q.l] && same[p.r,q.r]` 2. 迭代法 中序遍历比较|注意比较值，注意先判断None|
|102. 层次遍历|1. 迭代法 借助队列处理|注意区分值与节点|
|103.二叉树的锯齿形层序遍历| 102+flag|flag 只改变值的记录方式||
|104.二叉树的最大深度| 递归法 `D(n)=1+max(D(n.left),D(n.right))`||
|105.从前序与中序遍历序列构造二叉树| 递归法  |使用索引表存储索引|
|105.从后与中序遍历序列构造二叉树| 递归法  |使用索引表存储索引|


### AVL树

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|1382. 将二叉搜索树变平衡| 1.中序遍历获得有序数组 2. 分治法 中间划分平衡构建||