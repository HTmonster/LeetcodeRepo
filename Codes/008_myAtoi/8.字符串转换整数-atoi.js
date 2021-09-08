/*
 * @Author: Theo_hui
 * @Date: 2021-09-08 20:30:08
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=8 lang=javascript
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    var rst=0,symbol=1
    var i=0,status=0

    while(i<s.length){
        c=s[i]
        if(status==0){
            if(c==' '){
                i++
            }else{
                status=1
            }
        }else if(status==1){
            if(c=='+'){
                i++
            }else if(c=='-'){
                symbol=-1
                i++
            }
            status=2
        }else if(status==2){
            if(c<='9' && c>='0'){
                rst=rst*10+(c-'0')
                if(symbol==1 && rst>2147483647){
                    rst=2147483647
                    break
                }
                if(symbol==-1 && rst>2147483648){
                    rst=2147483648
                    break
                }
                i++
            }else{
                break
            }
        }
    }

    return rst*symbol
};
// @lc code=end

