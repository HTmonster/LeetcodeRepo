<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-03-08 19:52:10
-->

## 回溯法

### 模版
```python
def backtrack(...):
    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
```

|算法|要点|备注|
|-|-|-|
| [46. 全排列](https://leetcode-cn.com/problems/permutations/)|如果数组中以及包含该数字则退出||
