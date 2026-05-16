# ============================================================
# LeetCode #142 - Linked List Cycle II
# 日期：2026-05-15
# 难度：Medium
# 题目：https://leetcode.com/problems/linked-list-cycle-ii/
# ============================================================
#
# 【思路】快慢指针两阶段法
#
# 定义：
#   a = head 到环入口的距离
#   b = 环入口到相遇点的距离
#   c = 相遇点回到环入口的距离
#
# 数学推导：
#   快指针路程 = 慢指针路程 × 2
#   (a + 2b + c) = 2(a + b)  →  a = c
#
# 结论：相遇后一个指针回 head，两者同速，再次相遇即为环入口
#
# 【阶段一】快慢指针找相遇点（同 #141）
# 【阶段二】ptr 从 head 出发，slow 留原地，同速找环入口
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# ============================================================

class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        
        return None
