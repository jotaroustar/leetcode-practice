# LeetCode 438 - Find All Anagrams in a String
# 难度: Medium
# 提交日期: 2026-05-10
# 解法: 固定大小滑动窗口 + 字符频率比较
# 时间复杂度: O(n) n=len(s)
# 空间复杂度: O(1) 字符集固定26个字母
#
# 题目:
# 找s中所有p的字母异位词的起始索引
# 字母异位词:字母相同但顺序不同
#
# 思路:
# 窗口大小固定为len(p)
# 每次right加入新字符,窗口超过len(p)就移出left
# 窗口大小==len(p)时,比较window和p_count是否相等
#
# 与#3的区别:
# #3: 窗口大小不固定,用while动态缩小
# #438: 窗口大小固定,用if缩小(每次最多超出1个)
#
# 关键语法:
# Counter(p) → 一行统计字符频率
# window == p_count → 字典可以直接==比较内容
#
# 学到的:
# 1. 固定窗口:窗口超出就移出left,不用while
# 2. Counter是手动get(c,0)+1的简洁替代
# 3. 字典==比较不看顺序,只看key-value是否一致

class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter

        p_count = Counter(p)
        window = {}
        result = []
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if right - left + 1 > len(p):
                left_c = s[left]
                window[left_c] -= 1
                if window[left_c] == 0:
                    del window[left_c]
                left += 1

            if right - left + 1 == len(p):
                if window == p_count:
                    result.append(left)

        return result
