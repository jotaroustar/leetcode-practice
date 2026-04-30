# LeetCode 026 - Remove Duplicates from Sorted Array
# 难度: Easy
# 提交日期: 2026-04-30
# 解法: 双指针
# 时间复杂度: O(n)
# 空间复杂度: O(1) - 原地修改
#
# 题目:
# 给定升序数组,原地删除重复项,每个元素只保留一次
# 返回去重后的数组长度
#
# 思路:
# 利用"已排序"特性 - 重复元素必然相邻
# k指针: 记录下一个去重元素该放的位置
# i指针: 遍历数组寻找新元素
# 当 nums[i] != nums[i-1] 时,说明遇到新元素,放入nums[k]
#
# 模拟过程 nums = [0, 0, 1, 1, 1, 2]:
# k=1
# i=1: nums[1]=0 == nums[0]=0, 跳过
# i=2: nums[2]=1 != nums[1]=0, nums[1]=1, k=2 → [0,1,1,1,1,2]
# i=3: nums[3]=1 == nums[2]=1, 跳过
# i=4: nums[4]=1 == nums[3]=1, 跳过
# i=5: nums[5]=2 != nums[4]=1, nums[2]=2, k=3 → [0,1,2,1,1,2]
# 返回 3,前3个元素 [0,1,2] 是去重结果
#
# 学到的:
# 1. 双指针的"原地修改"模式
# 2. 利用数组特性(已排序)简化判断
# 3. 与 #283 Move Zeroes 是同一思路的变种

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # index for unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
        
#claude
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
