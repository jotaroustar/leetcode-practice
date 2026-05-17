# LeetCode 027 - Remove Element
# 难度: Easy
# 提交日期: 2026-05-03
# 解法: 双指针(快慢同向)
# 时间复杂度: O(n)
# 空间复杂度: O(1) - 原地修改
#
# 题目:
# 原地删除所有等于val的元素,返回新长度
# 元素顺序可以改变,后面的位置不重要
#
# 思路:
# slow指针记录"非val元素该放的位置"
# fast指针遍历数组
# nums[fast] != val 时,放到slow位置,slow+1
# 最后slow就是新长度
#
# 与 #283 Move Zeroes 对比:
# - 283: 判断"非0",最后还要把slow之后填0
# - 27 : 判断"非val",不需要填0(题目说后面不重要)
# 几乎一模一样的模板
#
# 学到的:
# 1. 双指针快慢同向模板的应用
# 2. 题目的细微差异决定模板的小调整

class Solution(object):
    def removeElement(self, nums, val):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

#双向解法(对撞双指针)
class Solution(object):
    def removeElement(self, nums, val):
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            else:
                left += 1
        return left
