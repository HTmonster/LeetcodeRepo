/*
 * @lc app=leetcode.cn id=13 lang=javascript
 *
 * [13] 罗马数字转整数
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {

    var ROMANS={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    var last=ROMANS[s[0]]
    var num=last
    for(var i=1;i<s.length;i++){
        var now=ROMANS[s[i]]
        if(now>last){
            now=now-2*last
        }
        num+=now
        last=now
    }

    return num

};
// @lc code=end

