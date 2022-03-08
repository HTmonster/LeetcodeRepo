'''
Description: 
Autor: HTmonster
Date: 2022-02-18 10:47:54
'''
#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 构建 diff数组
        diff=[0 for _ in range(n)]

        # 区间加法操作
        def increment(i,j,incr):
            nonlocal diff
            diff[i-1]+=incr
            if j<len(diff):
                diff[j]-=incr
            # print(i,j,incr,diff)
        
        # 取操作
        for book in bookings:
            i,j=book[0],book[1]
            incr=book[2]
            increment(i,j,incr)
            
        # 重建
        result=[diff[0],]
        for i in range(1,len(diff)):
            result.append(result[i-1]+diff[i])
        
        return result
            
# @lc code=end

