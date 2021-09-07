/*
 * @Author: Theo_hui
 * @Date: 2021-09-07 10:49:22
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var symbol=1
    if(x<0){
        symbol=-1
        x=-1*x
    }

    var rst=0

    while(x>0){
        rst=rst*10+x%10
        x=parseInt(x/10)
    }

    rst=symbol*rst
    if(rst<-2147483648||rst>2147483647){
        return 0
    }
    
    return rst

};
// @lc code=end

