<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-03-08 19:30:25
-->

## 动态规划法

##### 模板
```python

def 问题() :
    # dp(i,j)定义
    
    备忘录

    def dp(i,j):
        # 退出条件
        if i,j怎么怎么: return 返回值

        # 检查备忘录
        if (i,j) 在备忘录中: 
            return 直接返回值

        # 状态转换
        if 状态1条件:
            res=dp(状态1)
        else:
            取最值
            res=min(
                dp(状态a)+值1,   
                dp(状态b)+值2,   
                dp(状态c)+值3)   
        记录状态到备忘录中
        return 返回值
    # 问题
    return dp(开始值,开始值)
```


##### 动态规划法-一维

| 题目编号| 解题思路 | 备注 |
| ------ |-------- | ---- |
|070.爬楼梯|p[n]=p[n-1]+p[n-2] if n>2  elif n==2  2 else 1爬到第 n 级台阶的⽅法个数等于爬到 n - 1 的⽅法个数和爬到 n - 2 的⽅法个数之和。O(n)||
| [139. 单词拆分](https://leetcode-cn.com/problems/word-break/)|`p[i]` 为`s[i:]`的匹配问题，遍历每个字典，如果前缀匹配，则 `p[i]=p[i] or p[i+len(w)]`|为True就可以退出|

##### 动态规划法-二维

| 题目编号|题目内容 | 解题思路 | 备注 |
| ------ |---------|-------- | ---- |
|10. 正则表达式匹配| 给你一个字符串s和字符规律p, 请你实现一个支持'.'和'*'的正则表达式匹配| `ds[i][j]=any(ds[i][j-2],match(i,j-1) and ds[i-1][j]) if p[j-1]=='*' else all([match(i,j),ds[i-1][j-1]])` |空间换时间，记住历史信息|
|718.最长重复子数组|两个数组中 公共的 、长度最长的子数组的长度|1. 动态规划 `d[i][j]=d[i-1][j-1]+1 if i=j else 0` ![](http://latex.codecogs.com/gif.latex?O(M*N)\,O(M*N))|滑动窗口解法|
|1143.最长公共子序列|返回这两个字符串的最长 公共子序列 的长度|`d[i][j]=d[i-1][j-1]+1 if i=j else max(dp[i][j-1],dp[i-1][j])` ![](http://latex.codecogs.com/gif.latex?O(M*N)\,O(M*N))||
|5. 最长回文字符串| 给你一个字符串 s，找到 s 中最长的回文子串。|1.动态规划法(p[i,j]=True ^ s[i]==s[j]时是回文) ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(n^2)) <br> 2. 中心拓展法 ![](http://latex.codecogs.com/gif.latex?O(n^2)\,O(1)) |注意2中奇数个与偶数个的情况|
|72. 编辑距离|给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数| `p[i][j]` 代表 str1中0...i 和str2中0...j的编辑距离问题 `p[i][j]=p[i-1][j-1] if str1[i]==str2[j] else min(p[i-1][j]+1/插入,p[i][j-1]+1/删除,p[i-1][j-1]+1/替换`|| 

