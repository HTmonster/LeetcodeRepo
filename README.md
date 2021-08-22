### :city_sunrise:LeetcodeRepo 刷题仓库

> Leetcode的刷题记录仓库，刷的比较慢
>
> 语言使用Python，Golang,  javascript

#### :evergreen_tree:目录结构

- Codes （解题的代码）
- Solutions (难题的具体解题思路)
- Notes （算法的参考资料）

#### :bar_chart:目标与进度

| 目标                        | 进度                                                |
| --------------------------- | --------------------------------------------------- |
| 🔥 LeetCode 热题 HOT 100     | ![progress](https://progress-bar.dev/4/ "progress") |
| 👨‍💻 LeetCode 精选 TOP 面试题 | ![progress](https://progress-bar.dev/4/ "progress") |
| 简单 100                    | ![progress](https://progress-bar.dev/1/ "progress") |
| 中等 100                    | ![progress](https://progress-bar.dev/2/ "progress") |
| 困难 100                    | ![progress](https://progress-bar.dev/1/ "progress") |



#### :rainbow:思路总结

![](http://processon.com/chart_image/60a47231f346fb1df4240b29.png)

#### :rocket:题目思路大纲

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|   1. 两数之和    |   给定一个整数数组 nums 和一个整数目标值 target。请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。      | 1. 暴力穷举法 **时**:O(n^2) **空**:O(1) <br> 2.哈希法 **时**:O(n) **空**:O(n)      |   用哈希表来将找target-x的复杂度从O(n^2)降到O(1)    |
| 2. 两数相加 |  给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。| 模拟进位法 **O(max(m,n))** **O(1)** |可以作为大整数的实现方法|
|3. 无重复字符的最长子串|给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度|滑动窗口(快慢指针) **O(n)** **O(字符集大小)**| 字符最右下标hash表 空间换时间|
|4. 寻找两个正序数组的中位数|给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数。| 1.双指针移动法 **O(m+n)** **O(1)** <br> 2.二分排除法 **O(log(m+n))** **O(1)**|方法2同于有序数组的最小k值|

