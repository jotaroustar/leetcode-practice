# LeetCode 026 - Remove Duplicates from Sorted Array
# 难度: Easy
# 提交日期: 2026-04-30
# 解法: 双指针
# 时间复杂度: O(n)
# 空间复杂度: O(1) - 原地修改
#
# 思路:
# 因为数组已排序,重复元素必然相邻
# slow指向最后一个去重结果的位置
# fast遍历数组,遇到与nums[slow]不同的元素就放到slow+1位置
#
# 关键点:
# 1. 利用"已排序"特性,只比较相邻元素
# 2. 与Move Zeroes是同一思路的变种
#
# 学到的:
# - 双指针的两种风格(slow指向"下一空位" vs "最后有效位置")
# - 边界处理 (if not nums)

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
