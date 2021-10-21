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
| 🔥 LeetCode 热题 HOT 100     | ![progress](https://progress-bar.dev/6/ "progress") |
| 👨‍💻 LeetCode 精选 TOP 面试题 | ![progress](https://progress-bar.dev/8/ "progress") |
| 简单 100                    | ![progress](https://progress-bar.dev/3/ "progress") |
| 中等 100                    | ![progress](https://progress-bar.dev/5/ "progress") |
| 困难 100                    | ![progress](https://progress-bar.dev/2/ "progress") |



#### :rainbow:思路总结

![](http://processon.com/chart_image/60a47231f346fb1df4240b29.png)

#### :rocket:题目思路大纲

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|   1. 两数之和    |   给定一个整数数组 nums 和一个整数目标值 target。请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。      | 1. 暴力穷举法 ![](http://latex.codecogs.com/gif.latex?\\O(n^2)\,O(1)) <br> 2.哈希法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))  |   用哈希表来将找target-x的复杂度从![](http://latex.codecogs.com/gif.latex?O(n^2))降到![](http://latex.codecogs.com/gif.latex?O(1))    |
| 2. 两数相加 |  给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。| 模拟进位法 ![](http://latex.codecogs.com/gif.latex?O(max(m,n)\)\,O(1)) |可以作为大整数的实现方法|
|3. 无重复字符的最长子串|给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度|滑动窗口(快慢指针) $O(n),O(char\_cap)$| 字符最右下标hash表 空间换时间|
|4. 寻找两个正序数组的中位数|给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数。| 1.双指针移动法 ![](http://latex.codecogs.com/gif.latex?O(m+n)\,O(1)) <br> 2.二分排除法 ![](http://latex.codecogs.com/gif.latex?O(log(m+n)\)\,O(1))|方法2同于有序数组的最小k值|
|5. 最长回文字符串| 给你一个字符串 s，找到 s 中最长的回文子串。|1.动态规划法(p[i,j]=True ^ s[i]==s[j]时是回文) ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(n^2)) <br> 2. 中心拓展法 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(1)) |注意2中奇数个与偶数个的情况|
|6. Z字形变换|将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列|填充转换法 $O(n),O(n)$|1.不需要二维数组，直接append 2.善于使用flag(1 or -1)|
|7. 整数反转|给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。假设环境不允许存储 64 位整数（有符号或无符号）|直接转换法![](http://latex.codecogs.com/gif.latex?O(n)\,O(1))||
|8. 字符串转换整数|请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）|1.状态机转换法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(1)) 2.正则表达式法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(1))||
|9. 回文数|给你一个整数x, 如果x是一个回文整数，则返回true；否则，返回false|![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))||
|10. 正则表达式匹配| 给你一个字符串s和字符规律p, 请你实现一个支持'.'和'*'的正则表达式匹配|动态规划法，使用数组存储 ![](http://latex.codecogs.com/gif.latex?O(1)\,O(nm))|空间换时间，记住历史信息|