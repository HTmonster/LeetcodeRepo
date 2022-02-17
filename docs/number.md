<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-02-17 10:01:15
-->

## 数字

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|   1. 两数之和    |   给定一个整数数组 nums 和一个整数目标值 target。请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。      | 1. 暴力穷举法 ![](http://latex.codecogs.com/gif.latex?\\O(n^2)\,O(1)) <br> 2.哈希法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))  |   用哈希表来将找target-x的复杂度从![](http://latex.codecogs.com/gif.latex?O(n^2))降到![](http://latex.codecogs.com/gif.latex?O(1))    |
| 2. 两数相加 |  给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。| 模拟进位法 ![](http://latex.codecogs.com/gif.latex?O(max(m,n))\,O(1)) |可以作为大整数的实现方法|
|7. 整数反转|给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。假设环境不允许存储 64 位整数（有符号或无符号）|直接转换法![](http://latex.codecogs.com/gif.latex?O(n)\,O(1))||
|9. 回文数|给你一个整数x, 如果x是一个回文整数，则返回true；否则，返回false|![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))||
|12. 整数转罗马数字| 给你一个数字，转为罗马数字|模拟法，注意特殊情况4和9 ![](http://latex.codecogs.com/gif.latex?O(1)\,O(1))|由于搭配情况比较少，可以用暴力匹配法，用空间换时间|
|13. 罗马数字转整数| 给你一个罗马数字，将其转为整数| 注意特殊情况即可![](http://latex.codecogs.com/gif.latex?O(1)\,O(1))||