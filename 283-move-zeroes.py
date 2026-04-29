# LeetCode 283 - Move Zeroes
# 难度: Easy
# 提交日期: 2026-04-29
# 解法: 双指针
# 时间复杂度: O(n)
# 空间复杂度: O(1) - 原地修改
#
# 思路:
# slow指针记录非零元素该放的位置
# fast指针遍历数组,遇到非零就放到slow位置
# 最后把slow之后的位置全填0
#
# 学到的:
# 1. 双指针思想 - 一个指针管"读",一个指针管"写"
# 2. 原地修改 - 不开新数组,空间复杂度O(1)

class Solution(object):
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
