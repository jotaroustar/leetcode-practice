# LeetCode 009 - Palindrome Number
# 难度: Easy
# 提交日期: 2026-04-28
# 解法: 字符串反转比较
# 时间复杂度: O(n) - n是数字位数
# 空间复杂度: O(n) - 字符串占用
#
# 思路: 负数直接False,其他情况转字符串比较反转
# 关键语法: s[::-1] 反转字符串

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
