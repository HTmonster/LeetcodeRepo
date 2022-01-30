/*
 * @Description: 
 * @Autor: HTmonster
 * @Date: 2022-01-30 10:28:15
 */
/*
 * @lc app=leetcode.cn id=19 lang=javascript
 *
 * [19] 删除链表的倒数第 N 个结点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {

    left=toRemove=tail=head

    count=0
    while (tail!==null){
        if(count>n){
            left=left.next
        }
        if(count>=n){
            toRemove=toRemove.next
        }
        tail=tail.next
        count++
    }

    //特殊情况
    if(toRemove==head) {
        head=head.next
    }else{
        left.next=toRemove.next
    }
    delete toRemove

    return head

};
// @lc code=end

