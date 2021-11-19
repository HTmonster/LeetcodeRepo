/*
 * @lc app=leetcode.cn id=12 lang=javascript
 *
 * [12] 整数转罗马数字
 */

// @lc code=start
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const ROMANS={0:'',1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}

    var roman=''

    
    for(var i=1;i<10000;i*=10){
        var a=num%10
        num=parseInt(num/10)
        if(a==0){
            continue
        }else if(a==4||a==9){
            roman=ROMANS[i]+ROMANS[(a+1)*i]+roman
        }else{
            roman=ROMANS[parseInt(a/5)*5*i]+ROMANS[i].repeat(a%5)+roman
        }
        
    }

    return roman

};
// @lc code=end

