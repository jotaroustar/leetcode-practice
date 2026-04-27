# LeetCode 001 - Two Sum
# 难度: Easy
# 提交日期: 2026-04-27
# 解法: 哈希表(空间换时间)
# 时间复杂度: O(n)
# 空间复杂度: O(n)
# 运行时: 0ms (击败100%)
# 内存: 12.92MB (击败82.97%)
#
# 思路: 边遍历边把(数字 -> 索引)存入哈希表
# 对每个数字检查 target - num 是否已在表中,在就直接返回

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i
