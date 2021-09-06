/*
 * @Author: Theo_hui
 * @Date: 2021-09-06 11:17:56
 * @Descripttion: 
 */
/*
 * @lc app=leetcode.cn id=6 lang=javascript
 *
 * [6] Z 字形变换
 */

// @lc code=start
/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if(numRows ==1){
        return s
    }

    var storage = new Array()
    for(var i=0;i<numRows;i++){
        storage[i]=""
    }

    var line=0,flag=1

    for (const c of s){
        storage[line]=storage[line]+c
        if((flag==1 && line==numRows-1)|| (flag==-1 && line==0)){
            flag=-flag
        }
        line=line+flag
    }
    
    return storage.join("")
    

};
// @lc code=end

