<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-02-17 09:58:32
-->

## :train: 数组及字符串

### 🔢 前缀法

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|560.和为 K 的子数组|一个数组存储`前缀p` 一个数组存储`k-前缀p的个数`| 注意：`need=sum[j]-sum[i]`|

### 🛕 差分数组法

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|1109航班预订统计| `diff[i]=num[i]-num[i-1]` | 注意区间判断 和 i的含义 |

### 🏋️‍♀️ 滑动窗口法
#### 数组

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|4. 寻找两个正序数组的中位数| 1.双指针移动法 ![](http://latex.codecogs.com/gif.latex?O(m+n)\,O(1)) <br> 2.二分排除法 ![](http://latex.codecogs.com/gif.latex?O(log(m+n))\,O(1))|方法2同于有序数组的最小k值|
|11. 盛最多水的容器|双指针法 缩减 ![](http://latex.codecogs.com/gif.latex?O(n)\,O(1))||
|15. 三数之和| 先排序，单遍历+双指针 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(logn))|双指针为了排除一些已经搭配过的解，注意去重|
|16. 最接近的三数之和|同15,先排序,让后单遍历+双指针逼近 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(logn)) |优化: 得到target之后直接返回,因为没有更接近的空间了|
|18. 四数之和|同15，设目标为<i,j,k,l>, 1.先排序 2.搭配固定i,j 3.双指针逼近k,l![](http://latex.codecogs.com/gif.latex?O(n^3)\,O(logn))| 注意去重|

#### 字符串

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|076.最小覆盖子串|滑动窗口 right增→left增→right增| |