# LeetCode 141 - Linked List Cycle
# 难度: Easy
# 提交日期: 2026-05-14
# 解法: 快慢指针(Floyd判圈算法)
# 时间复杂度: O(n)
# 空间复杂度: O(1)
#
# 题目:
# 判断链表中是否有环
#
# 快慢指针思想:
# slow每次走1步,fast每次走2步
# 无环: fast先到终点(None),两者永不相遇
# 有环: fast会追上slow,两者必然相遇
#
# 类比: 两人在操场跑步
# 直道 → 快的人跑到终点,不会相遇
# 环形跑道 → 快的人必然追上慢的人
#
# while条件为什么是 fast and fast.next:
# fast每次走2步(fast.next.next)
# 必须确保fast和fast.next都不为None
# 否则访问fast.next.next会报错
#
# 学到的:
# 1. 快慢指针判断环的经典思路
# 2. fast走2步前必须检查fast和fast.next
# 3. 链表题中slow==fast比较的是节点对象,不是值

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
