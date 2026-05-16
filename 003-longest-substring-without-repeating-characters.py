# LeetCode 003 - Longest Substring Without Repeating Characters
# 难度: Medium
# 提交日期: 2026-05-010
# 解法: 滑动窗口 + 哈希表
# 时间复杂度: O(n)
# 空间复杂度: O(min(m,n)) m=字符集大小,n=字符串长度
#
# 题目:
# 找不含重复字符的最长子串的长度
#
# 滑动窗口思想:
# right扩大窗口,把s[right]加入window字典
# 当新加入的字符c出现次数>1(有重复)时,缩小窗口
# left右移,移出s[left],直到c的次数<=1
# 在while外更新max_len(此时窗口恰好无重复且最长)
#
# 与#209的对比:
# #209: while里更新min_len(找最短满足条件的窗口)
# #3:   while外更新max_len(找最长无重复的窗口)
#
# 踩过的坑:
# while条件用window[c]会报KeyError
# 原因:left移动时可能把c从window里删掉
# 修复:改用window.get(c, 0),key不存在返回0不报错
#
# 关键语法:
# window[c] = window.get(c, 0) + 1
#   → 有就+1,没有就设为1(安全计数)
# window.get(c, 0) > 1
#   → 安全访问,key不存在返回0不报错
# del window[left_c]
#   → 次数为0时删除key,保持字典干净
#
# 学到的:
# 1. 滑动窗口 + 哈希表的组合用法
# 2. window.get(key, default)比window[key]更安全
# 3. 更新位置的选择:找最短在while里,找最长在while外
# 4. 只检查新加入字符c是否重复,不用遍历整个窗口

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        window = {}
        max_len = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1   # 加入窗口

            while window.get(c, 0) > 1:         # 有重复就缩小
                left_c = s[left]
                window[left_c] -= 1
                if window[left_c] == 0:
                    del window[left_c]
                left += 1

            max_len = max(max_len, right - left + 1)  # 无重复时更新

        return max_len
