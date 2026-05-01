# LeetCode 344 - Reverse String
# 难度: Easy
# 提交日期: 2026-05-01
# 解法: 双指针(主推)/ 内置方法(炫技)
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 题目:
# 原地反转字符串数组,不能使用额外空间
#
# 解法1: 双指针(推荐学习)
# left从头开始,right从尾开始
# 交换两个位置的元素,然后向中间靠拢
# 直到 left >= right
#
# 学到的:
# 1. 双指针的"对撞型"用法(头尾向中间)
# 2. Python多重赋值: a, b = b, a 一行交换两个值
# 3. 区别于Move Zeroes/Remove Duplicates的"快慢型"双指针
#
# 解法2: 内置方法(知道即可)
# s.reverse() 一行搞定,但学不到算法思想
# 注意: s.reverse() 返回None,不能写 s = s.reverse()

class Solution(object):
    def reverseString(self, s):
        # 解法1: 双指针
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # 解法2(注释掉): 直接调用内置方法
        # s.reverse()
