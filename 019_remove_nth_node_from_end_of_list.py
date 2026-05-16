# ============================================================
# LeetCode #19 - Remove Nth Node From End of List
# 日期：2026-05-15
# 难度：Medium
# 题目：https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# ============================================================
#
# 【思路】哑节点 + 快慢指针固定间距法
#
# 核心：fast 先走 n 步建立间距，
#       fast 到终点时 slow 恰好在倒数第 n+1 个节点
#       执行 slow.next = slow.next.next 完成删除
#
# 哑节点作用：统一处理删除头节点的边界情况
#
# 时间复杂度：O(n)  一次遍历
# 空间复杂度：O(1)
# ============================================================

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy.next
