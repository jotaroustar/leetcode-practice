# LeetCode 209 - Minimum Size Subarray Sum
# 难度: Medium ← 你的第一道中等难度!
# 提交日期: 2026-05-07
# 解法: 滑动窗口
# 时间复杂度: O(n) - left和right各最多移动n次
# 空间复杂度: O(1)
#
# 题目:
# 找和 >= target 的最短连续子数组,返回长度
# 不存在返回0
#
# 滑动窗口思想:
# right指针:扩大窗口(向右移,加入新元素)
# left指针:缩小窗口(向右移,排除左边元素)
# 当窗口和 >= target:记录长度,尝试缩小
# 用while不用if:缩小后可能仍满足条件,继续缩
#
# 关键点:
# 1. min_len初始化为float('inf')表示"未找到"
# 2. 窗口长度 = right - left + 1
# 3. 最后判断是否找到: min_len == float('inf')则返回0
#
# 与双指针的关系:
# 滑动窗口是双指针的进化版
# 双指针:一快一慢同向移动
# 滑动窗口:right扩大,left根据条件缩小,窗口动态变化
#
# 学到的:
# 1. 滑动窗口模板: right扩大 + while条件成立就缩小
# 2. float('inf') 表示Python中的无穷大
# 3. while vs if: 缩小后仍可能满足条件要用while

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
