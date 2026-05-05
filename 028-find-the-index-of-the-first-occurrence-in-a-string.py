# LeetCode 028 - Find the Index of the First Occurrence in a String
# 难度: Easy
# 提交日期: 2026-05-03
# 解法: 暴力匹配 / Python内置方法
# 时间复杂度: O(n*m) - n=haystack长度, m=needle长度
# 空间复杂度: O(m) - 切片创建新字符串
#
# 题目:
# 找needle在haystack中第一次出现的下标
# 找不到返回-1
#
# 解法1: 暴力匹配
# 遍历haystack的每个可能起点
# 起点最大值: n - m (再往后剩余字符不够)
# 比较 haystack[i:i+m] == needle
#
# 解法2: Python内置方法(一行AC)
# return haystack.find(needle)
# - find()找不到返回-1,正好符合题目要求
# - index()找不到抛异常,不适合本题
#
# 进阶: KMP算法可以优化到O(n+m),后续学习
#
# 学到的:
# 1. 字符串切片 s[i:i+m] 取连续m个字符
# 2. 字符串比较 == 直接判断相等
# 3. find() vs index() 的区别
# 4. 边界处理:循环范围 range(n - m + 1)

class Solution(object):
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        
        if m == 0:
            return 0
        
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1
        
        # 解法2: 一行流
        # return haystack.find(needle)
