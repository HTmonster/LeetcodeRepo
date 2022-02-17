<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-02-17 09:56:45
-->


## 字符串

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|3. 无重复字符的最长子串|给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度|滑动窗口(快慢指针) $O(n),O(char\_cap)$| 字符最右下标hash表 空间换时间|
|5. 最长回文字符串| 给你一个字符串 s，找到 s 中最长的回文子串。|1.动态规划法(p[i,j]=True ^ s[i]==s[j]时是回文) ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(n^2)) <br> 2. 中心拓展法 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(1)) |注意2中奇数个与偶数个的情况|
|6. Z字形变换|将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列|填充转换法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(n))|1.不需要二维数组，直接append 2.善于使用flag(1 or -1)|
|8. 字符串转换整数|请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）|1.状态机转换法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(1)) 2.正则表达式法 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(1))||
|10. 正则表达式匹配| 给你一个字符串s和字符规律p, 请你实现一个支持'.'和'*'的正则表达式匹配|动态规划法，使用数组存储 ![](http://latex.codecogs.com/gif.latex?O(1)\,O(nm))|空间换时间，记住历史信息|