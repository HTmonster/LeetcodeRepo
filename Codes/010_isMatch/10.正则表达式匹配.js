/*
 * @lc app=leetcode.cn id=10 lang=javascript
 *
 * [10] 正则表达式匹配
 */

// @lc code=start
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
    // 1. 作弊法
    // var n=s.search('^'+p+'$')
    // if(n!=-1){
    //     return true
    // }else{
    //     return false
    // }

    // 2. 动态规划法
    var match=function(i,j){
        if(i==0){
            return false
        }else if(p[j-1]=="." || p[j-1]==s[i-1]){
            return true
        }else{
            return false
        }
    }

    //信息存储数组
    var ds=new Array();

    // i必须从0开始，因为可能有空匹配的情况 s='' p="a*b*c*"
    for(i=0;i<s.length+1;i++){
        
        ds[i]=new Array();
        if(i==0){
            ds[0][0]=true
        }else{
            ds[i][0]=false
        }

        for(j=1;j<p.length+1;j++){
            
            if(p[j-1]=="*"){
                //情况1 不匹配 例 p: ab*c=>ac  s：abc
                ds[i][j]=ds[i][j-2]
                
                //情况2 匹配   例 p: ab*c      s：abc=>ac  
                if(match(i,j-1)){
                    ds[i][j]=(ds[i-1][j]||ds[i][j])
                }
            }else{
                // 普通匹配了 例 p: ab*c=>b*c  s: abc=>b*c
                if(match(i,j)){
                    ds[i][j]=ds[i-1][j-1]
                }else{
                    ds[i][j]=false
                }
            }
        }
    }
    return ds[s.length][p.length]
};
// @lc code=end

