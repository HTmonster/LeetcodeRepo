<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2021-08-08 14:56:45
-->
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
| 简单 100                    | ![progress](https://progress-bar.dev/5/ "progress") |
| 中等 100                    | ![progress](https://progress-bar.dev/15/ "progress") |
| 困难 100                    | ![progress](https://progress-bar.dev/2/ "progress") |



#### :rainbow:思路总结

![](http://processon.com/chart_image/60a47231f346fb1df4240b29.png)


#### :rocket:题目思路大纲

##### 数据结构区分

| 数据结构                  | 思路                                            |
| -------------------------| --------------------------------------------------- |
| 字符串                   　| [字符串](./docs/string.md)|
| 数组                    | [数组](./docs/array.md)|
| 链表                    | [链表](./docs/linklist.md) |
| 树                    | [树](./docs/tree.md) |
| 数字                    | [数字](./docs/number.md)|

##### 动态规划法

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|10. 正则表达式匹配| 给你一个字符串s和字符规律p, 请你实现一个支持'.'和'*'的正则表达式匹配| `ds[i][j]=any(ds[i][j-2],match(i,j-1) and ds[i-1][j]) if p[j-1]=='*' else all([match(i,j),ds[i-1][j-1]])` |空间换时间，记住历史信息|
|718.最长重复子数组|两个数组中 公共的 、长度最长的子数组的长度|1. 动态规划 `d[i][j]=d[i-1][j-1]+1 if i=j else 0` ![](http://latex.codecogs.com/gif.latex?O(M*N)\,O(M*N))|<a href="#滑动窗口法">滑动窗口解法</a>|
|1143.最长公共子序列|返回这两个字符串的最长 公共子序列 的长度|`d[i][j]=d[i-1][j-1]+1 if i=j else max(dp[i][j-1],dp[i-1][j])` ![](http://latex.codecogs.com/gif.latex?O(M*N)\,O(M*N))||
|5. 最长回文字符串| 给你一个字符串 s，找到 s 中最长的回文子串。|1.动态规划法(p[i,j]=True ^ s[i]==s[j]时是回文) ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(n^2)) <br> 2. 中心拓展法 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(1)) |注意2中奇数个与偶数个的情况|
##### 滑动窗口法
| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|718.最长重复子数组|两个数组中 公共的 、长度最长的子数组的长度|||

##### 设计题

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|146.LRU缓存|请你设计并实现一个满足LRU（最近最少使用）缓存约束的数据结构|双向链表+hash表，双向链表保持顺序，hash快速存取|双向链表可以用一个假的tail和head避免删除检查|