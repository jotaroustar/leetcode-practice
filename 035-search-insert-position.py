# LeetCode 035 - Search Insert Position
# 难度: Easy
# 提交日期: 2026-05-07
# 解法: 暴力遍历 / 二分查找
# 时间复杂度: O(n) 暴力 / O(log n) 二分
# 空间复杂度: O(1)
#
# 题目:
# 给升序数组和目标值target
# 找target的下标,不存在则返回应该插入的位置
#
# 解法1: 暴力遍历(自己写的版本)
# 统计有多少个数比target小
# 这个数量就是target应该插入的位置
#
# 模拟 nums=[1,3,5,6], target=2:
# i=0: 1 < 2, count=1
# i=1: 3 > 2, 跳过
# 返回 count=1 ✅
#
# 解法2: 二分查找(标准解法,O(log n))
# 每次取中间值mid,和target比较
# target在右半边 → left = mid + 1
# target在左半边 → right = mid - 1
# 循环结束时left就是插入位置
#
# 为什么循环结束时return left:
# left > right时循环停止
# 此时left指向"第一个比target大的位置"
# 也就是target应该插入的位置
#
# 易错点:
# 1. self是Python保留字,不能当普通变量用
# 2. mid = (left + right) // 2 用整除
# 3. 二分的循环条件是 left <= right(不是 left < right)
#
# 学到的:
# 1. 暴力思路:"比target小的有几个,插在第几位"
# 2. 二分查找:每次砍掉一半,O(log n)
# 3. 二分是继双指针之后第二大核心算法思想

class Solution(object):
    def searchInsert(self, nums, target):
        # 解法1: 暴力遍历
        count = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < target:
                count += 1
        return count
暴力遍历（简化版）
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i

        # 解法2: 二分查找(注释掉,供对比学习)
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return left
