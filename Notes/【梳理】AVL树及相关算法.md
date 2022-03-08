<!--
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-03-08 20:03:02
-->
## 零、基础知识

### 1. 定义

> AVL树是一种**平衡**二叉树。

其递归**定义**为：

- 左右子树的**高度差**小于等于 1
- 其每一个子树均为**平衡二叉树**

#### 平衡因子

节点的平衡因子=左子树高度-右子树高度

> 故：平衡二叉树即所有结点的平衡因子的绝对值都不超过 1 的二叉树。

### 2. 两种基本平衡化操作

#### 右旋操作



#### 左旋操作



## 壹、AVL树的失衡调整

### 1. 左单旋转LL

**失衡原因：**在右子树插入右节点

### 2. 右单旋转RR

**失衡原因: ** 在左子树插入左节点


### 3.  先左旋后右旋LR

**失衡原因**：在右子树上插入左孩子导致AVL树失衡


### 4. 先右旋后左旋 RL

**失衡原因**：在左子树上插入右孩子导致AVL树失衡


### 总结

|**类型**|**使用情形**|
|-|-|
|单左旋|在左子树插入左孩子节点，使得平衡因子绝对值由1增至2|
|单右旋|在右子树插入右孩子节点，使得平衡因子绝对值由1增至2|
|先左旋后右旋|在左子树插入右孩子节点，使得平衡因子绝对值由1增至2|
|先右旋后左旋|在右子树插入左孩子节点，使得平衡因子绝对值由1增至2|


## 貳、AVL树相关算法

#### [108. 将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/)

- 递归
- 中间拆分 分治法

#### [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

- 同108
- 只是使用快慢指针 找中点 （快指针是慢指针的两倍）

#### [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

- 递归返回高度
- BF大于1时候之间返回不符合

#### [1382. 将二叉搜索树变平衡](https://leetcode-cn.com/problems/balance-a-binary-search-tree/)

1. 中序遍历获得有序数组
2. 有序数组中间拆分递归构建

```Python
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder=[]

        # 中序遍历
        def dfs(root):
            nonlocal inorder
            if root==None:
                return
            dfs(root.left)
            inorder.append(root.val)
            dfs(root.right)
        
        # 中间拆分建立
        def build(list):
            if len(list)<=0:
                return None
            # 中间拆分
            mid = int(len(list)/2)
            # 建立中间节点
            node = TreeNode(list[mid])
            # 递归构建左子树
            node.left =build(list[:mid])
            # 递归构建右子树
            node.right = build(list[mid+1:])
            return node

        # 1. 中序遍历得到有序数组
        dfs(root)
        # 2. 根据有序数组构建树
        return build(inorder)
```



> 巨人肩膀：

[详解 AVL 树（基础篇） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/34899732)

[数据结构图文解析之：AVL树详解及C++模板实现 - 蓝空 - 博客园 (cnblogs.com)](https://www.cnblogs.com/zswbky/p/8454078.html)