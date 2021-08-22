'''
Author: Theo_hui
Date: 2021-08-22 10:00:05
Descripttion: 
'''
#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    # 1.双指针移动中值法
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     # 总的长度
    #     total_len = len(nums1)+len(nums2)

    #     #双指针下标
    #     i=j=-1
    #     mid_num=None
    #     while (i+1)+(j+1) < int(total_len//2):
    #         i_num = nums1[i+1] if i+1<len(nums1) else float("inf") #取值nums1
    #         j_num = nums2[j+1] if j+1<len(nums2) else float("inf") #取值nums2

    #         #比较大小 指针移动
    #         if i_num<j_num:
    #             i+=1
    #             mid_num=i_num
    #         else:
    #             j+=1
    #             mid_num=j_num
    #     # 接着取下一个
    #     i_num = nums1[i+1] if i+1<len(nums1) else float("inf") #取值nums1
    #     j_num = nums2[j+1] if j+1<len(nums2) else float("inf") #取值nums2
    #     mid_num2= i_num if i_num<j_num else j_num

    #     #判断是奇数个还是偶数个
    #     return float(mid_num2) if total_len%2!=0 else float((mid_num+mid_num2)/2)
    
    # 2. 二分查找法(第k小数)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        #递归函数 获得两个数字中第k小的数
        def getkth(nums1,s1,nums2,s2,k):
            #获得两个区间长度
            len1,len2 = len(nums1)-1-s1,len(nums2)-1-s2

            #特殊情况 其中一个数组为空,返回另一个的第k小
            if len1==0:
                return nums2[s2+k]
            if len2==0:
                return nums1[s1+k]
            #递归出口 k=1
            if k==1:
                return min(nums1[s1+1],nums2[s2+1])
            else:
                #平分 每个数组比较的增加量
                mid_k=int(k/2)
                j1=mid_k if mid_k<=len1 else len1
                j2=mid_k if mid_k<=len2 else len2
                if nums1[s1+j1]<nums2[s2+j2]:
                    s1+=j1
                    newk=k-j1
                else:
                    s2+=j2
                    newk=k-j2
                return getkth(nums1,s1,nums2,s2,newk)
        
        #将奇数偶数合一
        k=(len(nums1)+len(nums2)+1)/2
        return float((getkth(nums1,-1,nums2,-1,math.ceil(k))+getkth(nums1,-1,nums2,-1,math.floor(k)))/2)


        
# @lc code=end

