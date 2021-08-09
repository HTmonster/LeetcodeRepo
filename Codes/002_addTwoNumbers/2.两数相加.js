/*
 * @Author: Theo_hui
 * @Date: 2021-08-09 10:42:02
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=2 lang=javascript
 *
 * [2] 两数相加
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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    
    let carry=0 //进位
    let head=null,tail=null //头尾节点


    while(l1!=null || l2!=null){
        let a=0,b=0
        if(l1!=null){
            a=l1.val
            l1=l1.next
        }
        if(l2!=null){
            b=l2.val
            l2=l2.next
        }

        sum = a+b+carry
        carry = Math.floor(sum / 10)
        var temp = new ListNode(sum %10)
        if(tail!=null){
            tail.next=temp
            tail=temp
        }else{
            head=tail=temp
        }
    }

    if(carry>0){
        tail.next = new ListNode(carry)
    }

    return head
};
// @lc code=end

